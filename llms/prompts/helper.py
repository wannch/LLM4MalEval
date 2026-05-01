from llms.prompts.constants import PyPI_MALICIOUS_PROMPT

from pathlib import Path
import json

EXAMPLE_FILE = Path(__file__).parent / "examples.json"
EXAMPLES = json.loads(EXAMPLE_FILE.read_text(encoding="utf-8"))
for example in EXAMPLES:
    with open(Path(__file__).parent / example['filepath'], 'r') as f:
        example['input'] = f.read()        

def build_prompt_messages(user_input:str):
    return [
                {
                    "role": "system", 
                    "content":PyPI_MALICIOUS_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]

"""
icl_examples: list of dict, each dict has 'input' and 'output' keys
Example:
[
    {
        'input': 'def example_code():\n    pass',
        'output': 'No, the code is not malicious because it does not perform any harmful actions.'
    },
    {
        'input': 'import os\nos.system("rm -rf /")',
        'output': 'Yes, the code is malicious because it attempts to delete all files on the system.'
    }
]
"""
def build_ICL_prompt_messages(user_input:str, icl_examples:list = EXAMPLES):
    
    messages = []
    messages.append(
                {
                    "role": "system", 
                    "content":PyPI_MALICIOUS_PROMPT
                }
            )
    
    for example in icl_examples:
        messages.append(
                {
                    "role": "user",
                    "content": example['input']
                }
            )
        messages.append(
                {
                    "role": "assistant",
                    "content": example['output']
                }
            )
    
    messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )
    
    return messages