from typing import Any, Dict, List, Optional
import gc
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from llms.llm_base import LLM

MODEL_ALIASES = {
    "deepseek-r1": "deepseek-ai/DeepSeek-R1",
    "deepseek-v3": "deepseek-ai/DeepSeek-V3-0324",
}

ALLOWED_LLM_LIST = [
    "deepseek-r1",
    "deepseek-v3",
    "deepseek-ai/DeepSeek-R1",
    "deepseek-ai/DeepSeek-V3-0324",
]


class DeepSeek(LLM):
    """Local Hugging Face inference wrapper for DeepSeek V3/R1 models."""

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
                f"Specified Model `{model_name_or_path}` is not supported for DeepSeek! "
                f"Allowed models: {ALLOWED_LLM_LIST}, or a local model directory."
            )
        if load_in_4bit and load_in_8bit:
            raise ValueError("Only one of load_in_4bit and load_in_8bit can be enabled.")

        self.model_name_or_path = MODEL_ALIASES.get(model_name_or_path, model_name_or_path)
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
                "Failed to load DeepSeek for local inference. Full DeepSeek-V3/R1 "
                "checkpoints are very large MoE models and may require the exact "
                "Transformers version, trust_remote_code support, enough GPU memory, "
                "or an inference runtime such as vLLM/SGLang for deployment."
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
            normalized_messages = self._normalize_messages(messages)
            input_ids = self.tokenizer.apply_chat_template(
                normalized_messages,
                add_generation_prompt=True,
                return_tensors="pt",
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

        response = outputs[0][input_ids.shape[-1]:]
        response_text = self.tokenizer.decode(response, skip_special_tokens=True)

        return response_text.strip()

    def _normalize_messages(self, messages: List[Dict]) -> List[Dict]:
        if self.model_name_or_path != "deepseek-ai/DeepSeek-R1":
            return messages

        system_parts = [
            msg["content"]
            for msg in messages
            if msg.get("role") == "system" and msg.get("content")
        ]
        if not system_parts:
            return messages

        normalized = [msg.copy() for msg in messages if msg.get("role") != "system"]
        system_prompt = "\n\n".join(system_parts)

        for msg in normalized:
            if msg.get("role") == "user":
                msg["content"] = f"{system_prompt}\n\n{msg.get('content', '')}"
                return normalized

        return [{"role": "user", "content": system_prompt}] + normalized

    def _terminator_ids(self) -> List[int]:
        terminators = []
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

    def _prompt_text_for_error(self, messages: List[Dict]) -> str:
        for message in reversed(messages):
            if message.get("role") == "user":
                return str(message.get("content", ""))
        return "\n".join(str(message.get("content", "")) for message in messages)

    def _build_llm_name(self, model_name_or_path: str) -> str:
        if model_name_or_path in MODEL_ALIASES:
            return model_name_or_path
        return os.path.basename(model_name_or_path.rstrip("/")).lower()


if __name__ == "__main__":
    llm = DeepSeek("deepseek-v3")

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
