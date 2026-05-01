from typing import Any, Dict, List, Optional, Tuple
import gc
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from llms.llm_base import LLM

MODEL_ALIASES = {
    "qwen2-7b": "Qwen/Qwen2-7B-Instruct",
    "qwen2-72b": "Qwen/Qwen2-72B-Instruct",
    "qwen2-7b-instruct": "Qwen/Qwen2-7B-Instruct",
    "qwen2-72b-instruct": "Qwen/Qwen2-72B-Instruct",
    "qwen3-8b": "Qwen/Qwen3-8B",
    "qwen3-14b": "Qwen/Qwen3-14B",
    "qwen3-32b": "Qwen/Qwen3-32B",
}

ALLOWED_LLM_LIST = [
    "qwen2-7b",
    "qwen2-72b",
    "qwen2-7b-instruct",
    "qwen2-72b-instruct",
    "qwen3-8b",
    "qwen3-14b",
    "qwen3-32b",
    "Qwen/Qwen2-7B-Instruct",
    "Qwen/Qwen2-72B-Instruct",
    "Qwen/Qwen3-8B",
    "Qwen/Qwen3-14B",
    "Qwen/Qwen3-32B",
]


class Qwen(LLM):
    """Local Hugging Face inference wrapper for Qwen2/Qwen3 chat models."""

    def __init__(
        self,
        model_name_or_path: str,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
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
                f"Specified Model `{model_name_or_path}` is not supported for Qwen! "
                f"Allowed models: {ALLOWED_LLM_LIST}, or a local model directory."
            )
        if load_in_4bit and load_in_8bit:
            raise ValueError("Only one of load_in_4bit and load_in_8bit can be enabled.")

        self.model_name_or_path = MODEL_ALIASES.get(model_name_or_path, model_name_or_path)
        self.llm_name = self._build_llm_name(model_name_or_path)
        self.base_url = base_url
        self.api_key = api_key

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
                "Failed to load Qwen for local inference. Qwen2 requires "
                "transformers>=4.37.0, and Qwen3 requires transformers>=4.51.0. "
                "Large variants such as Qwen2-72B also require enough GPU memory "
                "or a deployment runtime such as vLLM/SGLang."
            ) from exc

        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.eval()

    def chat(self, messages: List[Dict], **llm_args: Any):
        temperature = llm_args.pop("temperature", 0.6)
        top_p = llm_args.pop("top_p", 0.9)
        max_new_tokens = llm_args.pop("max_new_tokens", llm_args.pop("max_tokens", 2048))
        do_sample = llm_args.pop("do_sample", temperature > 0)
        enable_thinking = llm_args.pop("enable_thinking", None)
        return_thinking = llm_args.pop("return_thinking", False)

        try:
            chat_template_kwargs = {
                "add_generation_prompt": True,
                "return_tensors": "pt",
            }
            if enable_thinking is not None and self._is_qwen3_model():
                chat_template_kwargs["enable_thinking"] = enable_thinking

            input_ids = self.tokenizer.apply_chat_template(
                messages,
                **chat_template_kwargs,
            )
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

        output_ids = outputs[0][input_ids.shape[-1]:]
        if return_thinking:
            thinking, content = self._split_qwen3_thinking(output_ids)
            return {"thinking": thinking, "content": content}

        response_text = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        return response_text.strip()

    def _terminator_ids(self) -> List[int]:
        terminators = []
        for token in ("<|im_end|>", "<|endoftext|>"):
            token_id = self.tokenizer.convert_tokens_to_ids(token)
            if (
                isinstance(token_id, int)
                and token_id >= 0
                and token_id != self.tokenizer.unk_token_id
                and token_id not in terminators
            ):
                terminators.append(token_id)

        for token_id in (self.tokenizer.eos_token_id, self.tokenizer.pad_token_id):
            if token_id is not None and token_id not in terminators:
                terminators.append(token_id)

        return terminators

    def _input_device(self):
        if hasattr(self.model, "hf_device_map"):
            first_device = next(iter(self.model.hf_device_map.values()), None)
            if isinstance(first_device, int):
                return torch.device(f"cuda:{first_device}")
            if isinstance(first_device, str) and first_device not in {"cpu", "disk"}:
                return torch.device(first_device)

        return next(self.model.parameters()).device

    def _split_qwen3_thinking(self, output_ids) -> Tuple[str, str]:
        output_id_list = output_ids.tolist()
        think_end_id = self.tokenizer.convert_tokens_to_ids("</think>")
        if not isinstance(think_end_id, int) or think_end_id < 0:
            return "", self.tokenizer.decode(output_ids, skip_special_tokens=True).strip()

        try:
            split_idx = len(output_id_list) - output_id_list[::-1].index(think_end_id)
        except ValueError:
            split_idx = 0

        thinking = self.tokenizer.decode(output_ids[:split_idx], skip_special_tokens=True).strip()
        content = self.tokenizer.decode(output_ids[split_idx:], skip_special_tokens=True).strip()
        return thinking, content

    def _is_qwen3_model(self) -> bool:
        return "qwen3" in self.model_name_or_path.lower()

    def _prompt_text_for_error(self, messages: List[Dict]) -> str:
        for message in reversed(messages):
            if message.get("role") == "user":
                return str(message.get("content", ""))
        return "\n".join(str(message.get("content", "")) for message in messages)

    def _build_llm_name(self, model_name_or_path: str) -> str:
        if model_name_or_path in MODEL_ALIASES:
            return model_name_or_path
        return os.path.basename(model_name_or_path.rstrip("/")).lower()


class ALiBaBa(Qwen):
    """Backward-compatible name for the previous Qwen API wrapper."""


if __name__ == "__main__":
    llm = Qwen("Qwen/Qwen2-72B-Instruct")

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
