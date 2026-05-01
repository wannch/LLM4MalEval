import os
from typing import Dict
from openai import OpenAI

from llms.llm_base import LLM

ALLOWED_LLM_LIST = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o',
    'gpt-4o-mini',
    'gpt-5.1',
    'gpt-5.2',
    'gpt-5.2-codex'
]

class GPT(LLM):

    def __init__(self, model_name_or_path: str, base_url: str = None, api_key: str = None):
        super().__init__()

        if model_name_or_path not in ALLOWED_LLM_LIST:
            raise ValueError(f"Specified Model `{model_name_or_path}` is not supported for GPT! Allowed models: {ALLOWED_LLM_LIST}")

        self.model = model_name_or_path

        # Get API key from parameter or environment variable
        self.base_url = base_url or os.getenv('OPENAI_API_BASE_URL')
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')

        if not self.base_url:
            raise ValueError("OpenAI API base URL must be provided either as parameter or set as OPENAI_API_BASE_URL environment variable")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided either as parameter or set as OPENAI_API_KEY environment variable")

        self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

        if '/' in model_name_or_path:
            self.llm_name = model_name_or_path.split('/')[-1].lower()
        else:
            self.llm_name = model_name_or_path

    def chat(self, messages, **llm_args):
        resp = self.client.responses.create(
            model=self.model,
            stream=True,
            input=messages,
            reasoning={"effort": "high"},
            **llm_args
        )

        stream_output = ""
        with resp as stream:
            for event in stream:
                if event.type == "response.output_text.delta":
                    stream_output += event.delta
                if event.type == "response.completed":
                    try:
                        llm_output = event.to_dict()["response"]["output"][0]["content"][0]["text"]
                    except KeyError:
                        llm_output = event.to_dict()["response"]["output"][1]["content"][0]["text"]
        try:
            return llm_output.strip()
        except UnboundLocalError:
            return stream_output.strip()

        # try:
        #     response = self.client.chat.completions.create(
        #         model=self.model,
        #         messages=messages,
        #         **llm_args
        #     )
        #     content = response.choices[0].message.content.strip()
        #     return content
        # except Exception as e:
        #     return f'[ERROR]: {str(e)}'

if __name__ == '__main__':
    # Example usage - replace with your actual API key
    # You can also set OPENAI_API_KEY environment variable
    llm = GPT('gpt-3.5-turbo', api_key='your-openai-api-key-here')

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello, who are you?"
        }
    ]

    result = llm.chat(messages, temperature=0.7, max_tokens=150)
    print(result)
