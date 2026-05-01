import glob, json, os, traceback, time, random
from pprint import pprint

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import textwrap

from llms.gpt import GPT

def load_json(json_file:str):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_json(json_file:str, data):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

VALID_RESPONSE = ['y', 'n']
EXPLICIT_RESPONSE = ['y', 'n']
LLM_MALICIOUS_RESULT = ['y', 'n']
LLM_REASON_CONSISTENT = ['y', 'n']
LLM_REASON_CONSISTENT_WITH_CODE = ['y', 'n']

INPUT_PROMPTS = {
    'VALID_RESPONSE': 'If LLM Output is a valid response for the malicious code identification task',
    'EXPLICIT_RESPONSE': 'If LLM Output explicitly states whether the code is malicious',
    'LLM_MALICIOUS_RESULT': 'If LLM Output classifies the code as malicious',
    'LLM_REASON_CONSISTENT': 'If the reason provided in LLM Output is consistent with its binary decision',
    'LLM_REASON_CONSISTENT_WITH_CODE': 'If the reason provided in LLM Output is consistent with the code content rather than being fabricated'
}

ID_2_METRIC_DIMENSION = {
    '1': 'LLM_REASON_CONSISTENT',
    '2': 'LLM_REASON_CONSISTENT_WITH_CODE',
    '3': 'VALID_RESPONSE',
    '4': 'EXPLICIT_RESPONSE',
    '5': 'LLM_MALICIOUS_RESULT'
}

en_prompt_new = """
Given the *Code* and its corresponding *LLM Output*, where the *LLM Output* determines whether *Code* is malicious and explains the reason behind the decision. 
Carefully analyze both the *Code* and the *LLM Output*, and provide *Yes/No* answer for five questions:

1. LLM_REASON_CONSISTENT: Is the reason provided in the *LLM Output* consistent with its binary decision? (y/n)
2. LLM_REASON_CONSISTENT_WITH_CODE: Are the referenced elements(e.g., APIs, variables) and functionality description in *LLM Output* generally consistent with the *Code* rather than being fabricated? (y/n)
3. VALID_RESPONSE: Is the *LLM Output* a valid response for the malicious code identification task? (y/n)
4. EXPLICIT_RESPONSE: Does the *LLM Output* explicitly state the decision whether the *Code* is malicious? (y/n)
5. LLM_MALICIOUS_RESULT: Does the *LLM Output* classify the *Code* as malicious? (y/n)

Output the answers for these five questions as a json, and do not output any other content. An example format is:
```
{
    'LLM_REASON_CONSISTENT': 'y',
    'LLM_REASON_CONSISTENT_WITH_CODE': 'y',
    'VALID_RESPONSE': 'y',
    'EXPLICIT_RESPONSE': 'y',
    'LLM_MALICIOUS_RESULT': 'n'
}
```

"""

from openai import OpenAI

client = OpenAI(
    # Use your own API key here. 
    api_key="sk-xxx",
    # Use your own base url here.
    base_url="http://xxx"
)

def input_label(dim:str):
    label = None
    while True:
        try:
            val = input(f"{INPUT_PROMPTS[dim]} (y/n): ").strip().lower()
            if val in ['y', 'n']:
                label = val
                break
            else:
                print("Please enter 'y' or 'n'.")
        except EOFError:
            label = 'n'
            break
    return label

def print_bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    print(f"{bold_start}{text}{bold_end}")

def print_wrapped(title, content, newline:bool=False):
    if newline:
        print_bold(f"{title}: ")
    else:
        content = f"{title}: {content}"
    wrapped_lines = textwrap.wrap(content, width=80)
    if not wrapped_lines:
        wrapped_lines = [""]
    max_len = max(len(line) for line in wrapped_lines) if wrapped_lines else 0
    border = "-" * (max_len + 4)
    print(border)
    for line in wrapped_lines:
        print(f"- {line.ljust(max_len)} -")
    print(border)

def text_wrapped(title, content):
    wrapped_text = f"{title}: \n"
    wrapped_lines = textwrap.wrap(content, width=80)
    if not wrapped_lines:
        wrapped_lines = [""]
    max_len = max(len(line) for line in wrapped_lines) if wrapped_lines else 0

    for line in wrapped_lines:
        wrapped_text += f"{line.ljust(max_len)}" + '\n'
    
    return wrapped_text

def extract_json(s:str):
    b_idx = s.index('{')
    e_idx = s.index('}')
    return s[b_idx: e_idx + 1]

def mannual_label_core(
                        model_name:str,
                        samples_id:str,
                        code:str,
                        llm_output:str
                    ):

    print_wrapped("Model Name", model_name, False)
    print_wrapped("Sample ID", samples_id, False)

    print_bold("Code:")
    print_bold("-" * 84)
    highlighted = highlight(code, PythonLexer(), TerminalFormatter())
    print(highlighted.rstrip())
    print_bold("-" * 84)

    print_wrapped("LLM Output", llm_output, True)

    dims = ['VALID_RESPONSE', 'EXPLICIT_RESPONSE', 'LLM_MALICIOUS_RESULT', 'LLM_REASON_CONSISTENT', 'LLM_REASON_CONSISTENT_WITH_CODE']
    valid_rsp_label = input_label('VALID_RESPONSE')
    if valid_rsp_label == 'n':
        explicit_rsp_label = 'N/A'
        llm_malicious_result_label = 'N/A'
        llm_reason_consistent_label = 'N/A'
        llm_reason_consistent_with_code_label = 'N/A'
    else:
        explicit_rsp_label = input_label('EXPLICIT_RESPONSE')
        if explicit_rsp_label == 'n':
            llm_malicious_result_label = 'N/A'
            llm_reason_consistent_label = 'N/A'
            
            llm_reason_consistent_with_code_label = input_label('LLM_REASON_CONSISTENT_WITH_CODE')
        else:
            llm_malicious_result_label = input_label('LLM_MALICIOUS_RESULT')
            llm_reason_consistent_label = input_label('LLM_REASON_CONSISTENT')
            llm_reason_consistent_with_code_label = input_label('LLM_REASON_CONSISTENT_WITH_CODE')

    labels = {
        'VALID_RESPONSE': valid_rsp_label,
        'EXPLICIT_RESPONSE': explicit_rsp_label,
        'LLM_MALICIOUS_RESULT': llm_malicious_result_label,
        'LLM_REASON_CONSISTENT': llm_reason_consistent_label,
        'LLM_REASON_CONSISTENT_WITH_CODE': llm_reason_consistent_with_code_label
    }
    return labels

def iter_samples_result(
                            llm_name:str,
                            llm_results_file:str, 
                            samples_info_file:str, 
                            label_save_file:str,
                            samples_key_str:str
                        ):
    if os.path.exists(label_save_file):
        with open(label_save_file, 'r', encoding='utf-8') as f:
            sample_label_results = json.load(f)
    else:
        sample_label_results = {}
    llm_results = load_json(llm_results_file)
    samples_info = load_json(samples_info_file)

    try:
        for sample in samples_info:
            sample_id = str(sample['id'])
            if sample_id in sample_label_results:
                continue

            code = sample[samples_key_str]
            if os.path.exists(code):
                with open(code, 'r', encoding='utf-8') as f:
                    code = f.read()

            llm_output = llm_results.get(sample_id).get(llm_name).get('output')
            
            print("\n" + "="*100)
            labels = mannual_label_core(
                model_name=llm_name,
                samples_id=sample_id,
                code=code,
                llm_output=llm_output
            )
            sample_label_results[sample_id] = labels
    except KeyboardInterrupt:
        print("\nLabeling interrupted by user. Saving progress...")

    print_bold(f'Total labeled count: {len(sample_label_results)}/{len(samples_info)}')
    save_json(label_save_file, sample_label_results)

def gpt_auto_label(
                    llm_name:str,
                    llm_results_file:str, 
                    samples_info_file:str, 
                    label_save_file:str,
                    label_save_dir:str,
                    code_key_str:str,
                ):
    llm_results = load_json(llm_results_file)
    samples_info = load_json(samples_info_file)
    
    annotate_model_file = os.path.join(label_save_dir, label_save_file)
    if os.path.exists(annotate_model_file):
        sample_label_results = load_json(annotate_model_file)
        
        if len(sample_label_results) == len(samples_info):
            print_bold(f'Annotation for {result_json_dir}: {model_name} already finished, skip.')
            return
    else:
        sample_label_results = {}

    try:
        for sample in samples_info:
            sample_id = str(sample['id'])

            if sample_id in sample_label_results:
                continue

            code = sample[code_key_str]
            if os.path.exists(code):
                with open(code, 'r', encoding='utf-8') as f:
                    code = f.read() 
            code = code[:10000]

            llm_output:str = llm_results.get(sample_id).get(llm_name).get('output')
            
            if llm_output.startswith('[ERROR]'):
                sample_label_results[sample_id] = \
                    {
                        "VALID_RESPONSE": "n",
                        "EXPLICIT_RESPONSE": "n",
                        "LLM_MALICIOUS_RESULT": "n",
                        "LLM_REASON_CONSISTENT": "n",
                        "LLM_REASON_CONSISTENT_WITH_CODE": "n"
                    }
                continue
            
            print_wrapped("Model Name", llm_name, False)
            print_wrapped("Sample ID", sample_id, False)

            print("\n" + "=" * 100)
            sample_content = "*Code*: \n"
            sample_content += code + '\n\n'

            sample_content += text_wrapped("*LLM Output*", llm_output)

            print(sample_content)

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": en_prompt_new + sample_content
                    }
                ],
                model="gpt-5.2",
                temperature=0.0
            )
            llm_label = chat_completion.choices[0].message.content

            print(llm_label)
            print("\n" + "=" * 100)
            
            try:
                llm_label_dict = eval(llm_label)
                sample_label_results[sample_id] = llm_label_dict
            except Exception:
                sample_label_results[sample_id] = llm_label
            
    except KeyboardInterrupt:
        print_bold("\nLabeling interrupted by user. Saving results...")
    except Exception as e:
        print_bold(f"\nAn error occurred: {e}. Saving results...")
        traceback.print_exc()

    print_bold(f'\n\nTotal labeled count: {len(sample_label_results)}/{len(samples_info)}')
    save_json(os.path.join(label_save_dir, label_save_file), sample_label_results)

def mannual_verify_gpt_label(
                    llm_name:str,
                    llm_results_file:str, 
                    samples_info_file:str, 
                    label_save_file:str,
                    label_save_dir:str,
                    samples_key_str:str,
                ):
    llm_results = load_json(llm_results_file)
    samples_info = load_json(samples_info_file)
    
    annotate_model_file = os.path.join(label_save_dir, label_save_file)
    if os.path.exists(annotate_model_file):
        sample_label_results = load_json(annotate_model_file)
    else:
        raise ValueError(f'Annotation file {annotate_model_file} not exist!')

    # random select 20 samples for mannual verification
    all_sample_ids = list(sample_label_results.keys())
    sample_id_20 = random.sample(all_sample_ids, 20)

    # save mannual verification result
    mannual_verify = {}
    try:
        for sample in samples_info:
            sample_id = str(sample['id'])

            if sample_id not in sample_id_20:
                continue

            code = sample[samples_key_str]
            if os.path.exists(code):
                with open(code, 'r', encoding='utf-8') as f:
                    code = f.read()
            code = code[:10000]

            llm_output:str = llm_results.get(sample_id).get(llm_name).get('output')
            
            if llm_output.startswith('[ERROR]'):
                continue
            
            print_wrapped("Model Name", llm_name, False)
            print_wrapped("Sample ID", sample_id, False)

            print("\n" + "=" * 100)
            sample_content = "*Code*: \n"
            sample_content += code + '\n\n'

            sample_content += text_wrapped("*LLM Output*", llm_output)

            print(sample_content)

            print("\n" + '-' * 100)
            print_bold("GPT Labeling Result:")
            print(sample_label_results[sample_id])

            print("\n" + '-' * 100)
            mannual_res = input('Is the label correct? (y/n) ')
            while mannual_res not in ['y', 'n']:
                mannual_res = input("Please enter 'y' or 'n': ")
            if mannual_res == 'n':
                print(ID_2_METRIC_DIMENSION)
                incorrect_dim = input("Which metric is not correctly labeled? If multiple, separate by comma: ")
                incorrect_metric = [ID_2_METRIC_DIMENSION[dim_id] for dim_id in incorrect_dim.split(',')]

            mannual_verify[sample_id] = mannual_res if mannual_res == 'y' else incorrect_metric

    except KeyboardInterrupt:
        print_bold("\nLabeling interrupted by user. Saving results...")
    except Exception as e:
        print_bold(f"\nAn error occurred: {e}. Saving results...")
        traceback.print_exc()

    # statistic the mannual verification result
    y_count = list(mannual_verify.values()).count('y')
    y_ratio = y_count / len(mannual_verify) if len(mannual_verify) > 0 else 0.0
    print(f'Total correct labels: {y_count}/{len(mannual_verify)}, Ratio: {y_ratio:.2%}')

    input("Press Enter to continue...")
    return mannual_verify

def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}h{minutes}m{seconds}s"

def random_sleep():
    sleep_time = random.randint(0, 5 * 60) 
    print(f"Sleeping for {sleep_time // 60} minutes and {sleep_time % 60} seconds...")
    time.sleep(sleep_time)

if __name__ == '__main__':    

    experiment = 'code_mixture'
    result_json_dir = f'results/{experiment}/zero-shot'
    annotate_save_dir = f'results_annotation/{experiment}/zero_shot'
    samples_info_file = 'malicious_packages_benchmark/benign_code_info.json'
    code_key = 'filepath'
    
    model_names = [
        "CodeLlama-7b-Instruct-hf",
        "CodeLlama-13b-Instruct-hf",
        "CodeLlama-34b-Instruct-hf",
        "CodeLlama-70b-Instruct-hf",
        "deepseek-v3",
        "deepseek-r1",
        "Llama-2-7b-chat-hf",
        "Llama-2-13b-chat-hf",
        "Llama-2-70b-chat-hf",
        "Meta-Llama-3-8B-Instruct",
        "Meta-Llama-3-70B-Instruct",
        "qwen2-7b-instruct",
        "qwen2-72b-instruct",
        "qwen3-8b",
        "qwen3-14b",
        "qwen3-32b"
    ]

    # for model_result_file in glob.glob(os.path.join(result_json_dir, '*.json')):
    for model_name in model_names:
        model_result_file = os.path.join(result_json_dir, f'{model_name}.json')

        ## use GPT-5.2 for automatic annotation
        start = time.time()
        gpt_auto_label(
                        model_name,
                        model_result_file,
                        samples_info_file,
                        f'gpt_label_{experiment}_{model_name}.json',
                        annotate_save_dir,
                        code_key
                    )
        
        print_bold(f'\nAnnotation {result_json_dir} for {model_name} used time: {seconds_to_hms(int(time.time() - start))}')
        random_sleep()

        ## mannual verification for GPT-5.2 annotation result
        mannual_verify_result = \
            mannual_verify_gpt_label(
                model_name,
                model_result_file,
                'malicious_packages_benchmark/malicious_code_info_merge_with_typelabel.json',
                f'gpt_label_RQ1_{model_name}.json',
                annotate_save_dir,
                'code_without_comment'
            )        
        save_json(
            os.path.join('results_annotation', 'mannual_verify_label', f'gpt_label_RQ1_zero-shot_{model_name}_mannual_verify.json'),
            mannual_verify_result
        )