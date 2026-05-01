from typing import Any, Dict, List, Optional
import gc
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from llms.llm_base import LLM

ALLOWED_LLM_LIST = [
    "meta-llama/Llama-2-7b-chat-hf",
    "meta-llama/Llama-2-13b-chat-hf",
    "meta-llama/Llama-2-70b-chat-hf",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "meta-llama/Meta-Llama-3-70B-Instruct",
    "codellama/CodeLlama-7b-Instruct-hf",
    "codellama/CodeLlama-13b-Instruct-hf",
    "codellama/CodeLlama-34b-Instruct-hf",
    "meta-llama/CodeLlama-70b-Instruct-hf",
]


class Llama(LLM):
    """Local Hugging Face inference wrapper for Llama and CodeLlama chat models."""

    def __init__(
        self,
        model_name_or_path: str,
        torch_dtype: Any = "auto",
        device_map: Optional[str] = "auto",
        trust_remote_code: bool = True,
        local_files_only: bool = False,
        load_in_4bit: bool = False,
        load_in_8bit: bool = False,
        max_memory: Optional[Dict] = None,
        tokenizer_kwargs: Optional[Dict[str, Any]] = None,
        model_kwargs: Optional[Dict[str, Any]] = None,
        **_: Any,
    ):
        super().__init__()

        if model_name_or_path not in ALLOWED_LLM_LIST and not os.path.isdir(model_name_or_path):
            raise ValueError(
                f"Specified Model `{model_name_or_path}` is not supported for Llama! "
                f"Allowed models: {ALLOWED_LLM_LIST}, or a local model directory."
            )
        if load_in_4bit and load_in_8bit:
            raise ValueError("Only one of load_in_4bit and load_in_8bit can be enabled.")

        self.model_name_or_path = model_name_or_path
        self.llm_name = self._build_llm_name(model_name_or_path)

        tokenizer_load_kwargs = {
            "trust_remote_code": trust_remote_code,
            "local_files_only": local_files_only,
            **(tokenizer_kwargs or {}),
        }
        model_load_kwargs = {
            "trust_remote_code": trust_remote_code,
            "local_files_only": local_files_only,
            **(model_kwargs or {}),
        }

        if torch_dtype is not None:
            model_load_kwargs["torch_dtype"] = torch_dtype
        if device_map is not None:
            model_load_kwargs["device_map"] = device_map
        if max_memory is not None:
            model_load_kwargs["max_memory"] = max_memory
        if load_in_4bit:
            model_load_kwargs["load_in_4bit"] = True
        if load_in_8bit:
            model_load_kwargs["load_in_8bit"] = True

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name_or_path,
                **tokenizer_load_kwargs,
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name_or_path,
                **model_load_kwargs,
            )
        except Exception as exc:
            raise RuntimeError(
                "Failed to load Llama for local inference. Meta Llama models are "
                "gated on Hugging Face, so the environment must have access to the "
                "model repo. Large variants such as 70B also require enough GPU "
                "memory or a deployment runtime such as vLLM/SGLang."
            ) from exc

        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.eval()

    def chat(self, messages: List[Dict], **llm_args: Any):
        temperature = llm_args.pop("temperature", 0.6)
        top_p = llm_args.pop("top_p", 0.9)
        max_new_tokens = llm_args.pop("max_new_tokens", llm_args.pop("max_tokens", 2048))
        do_sample = llm_args.pop("do_sample", temperature > 0)

        try:
            input_ids = self._build_input_ids(messages)
            input_ids = input_ids.to(self._input_device())

            generation_kwargs = {
                "max_new_tokens": max_new_tokens,
                "eos_token_id": self._terminator_ids(),
                "pad_token_id": self.tokenizer.pad_token_id,
                "do_sample": do_sample,
                **llm_args,
            }
            if do_sample:
                generation_kwargs["temperature"] = temperature
                generation_kwargs["top_p"] = top_p

            with torch.no_grad():
                outputs = self.model.generate(input_ids, **generation_kwargs)
        except torch.OutOfMemoryError:
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            prompt_text = self._prompt_text_for_error(messages)
            return (
                f"[ERROR]: CUDA Out of Memory - Processing {len(prompt_text)} chars "
                f"with {len(prompt_text.split())} words."
            )
        except Exception as exc:
            return f"[ERROR]: {type(exc).__name__} - {str(exc)}"

        response = outputs[0][input_ids.shape[-1]:]
        response_text = self.tokenizer.decode(response, skip_special_tokens=True)

        return response_text.strip()

    def _build_input_ids(self, messages: List[Dict]):
        try:
            return self.tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                return_tensors="pt",
            )
        except Exception:
            prompt = self._format_prompt(messages)
            return self.tokenizer(prompt, return_tensors="pt").input_ids

    def _format_prompt(self, messages: List[Dict]) -> str:
        if self._is_llama3_model():
            return self._format_llama3_prompt(messages)
        return self._format_inst_prompt(messages)

    def _format_llama3_prompt(self, messages: List[Dict]) -> str:
        prompt = "<|begin_of_text|>"
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            prompt += f"<|start_header_id|>{role}<|end_header_id|>\n\n{content}<|eot_id|>"
        prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
        return prompt

    def _format_inst_prompt(self, messages: List[Dict]) -> str:
        system_prompt = ""
        turns = []
        for message in messages:
            role = message.get("role")
            content = message.get("content", "")
            if role == "system":
                system_prompt = content if not system_prompt else f"{system_prompt}\n\n{content}"
            else:
                turns.append({"role": role, "content": content})

        prompt = ""
        pending_user = None
        first_user = True

        for message in turns:
            role = message.get("role")
            content = message.get("content", "")
            if role == "user":
                if first_user and system_prompt:
                    content = f"<<SYS>>\n{system_prompt}\n<</SYS>>\n\n{content}"
                pending_user = content
                first_user = False
            elif role == "assistant":
                if pending_user is None:
                    prompt += f"{content} </s>"
                else:
                    prompt += f"<s>[INST] {pending_user.strip()} [/INST] {content.strip()} </s>"
                    pending_user = None

        if pending_user is not None:
            prompt += f"<s>[INST] {pending_user.strip()} [/INST]"

        return prompt

    def _terminator_ids(self) -> List[int]:
        terminators = []

        for token_id in (self.tokenizer.eos_token_id, self.tokenizer.pad_token_id):
            if token_id is not None and token_id not in terminators:
                terminators.append(token_id)

        eot_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        if (
            isinstance(eot_id, int)
            and eot_id >= 0
            and eot_id != self.tokenizer.unk_token_id
            and eot_id not in terminators
        ):
            terminators.append(eot_id)

        return terminators

    def _input_device(self):
        if hasattr(self.model, "hf_device_map"):
            first_device = next(iter(self.model.hf_device_map.values()), None)
            if isinstance(first_device, int):
                return torch.device(f"cuda:{first_device}")
            if isinstance(first_device, str) and first_device not in {"cpu", "disk"}:
                return torch.device(first_device)

        return next(self.model.parameters()).device

    def _is_llama3_model(self) -> bool:
        return "llama-3" in self.model_name_or_path.lower()

    def _prompt_text_for_error(self, messages: List[Dict]) -> str:
        for message in reversed(messages):
            if message.get("role") == "user":
                return str(message.get("content", ""))
        return "\n".join(str(message.get("content", "")) for message in messages)

    def _build_llm_name(self, model_name_or_path: str) -> str:
        return os.path.basename(model_name_or_path.rstrip("/"))


if __name__ == "__main__":
    llm = Llama("meta-llama/Meta-Llama-3-70B-Instruct")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Hello, who are you?",
        },
    ]
    start = time.time()
    result = llm.chat(messages, temperature=0.6, top_p=0.9)
    print(result)
    print(f"Chat used time: {time.time() - start:.2f}s")
