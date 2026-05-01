from llms.deepseek import DeepSeek, ALLOWED_LLM_LIST as DEEPSEEK_ALLOWED_LLM_LIST
from llms.qwen import Qwen, ALLOWED_LLM_LIST as QWEN_ALLOWED_LLM_LIST
from llms.llama import Llama, ALLOWED_LLM_LIST as LLAMA_ALLOWED_LLM_LIST
from llms.prompts.helper import build_prompt_messages, build_ICL_prompt_messages
from llms.llm_base import LLM

import time, os, json, traceback, pprint
from loguru import logger
import argparse

benchmark_dir = 'malicious_packages_benchmark/'
samples_json = 'malicious_code_info_merge_with_typelabel.json'
benign_info_json = 'benign_code_info.json'

def print_results(id, res:str, used_time, **kwargs):
    s = '\n' + '=' * 100 + '\n'
    s += f'For {id}: \n'
    s += res + '\n'
    s += '-' * 100 + '\n'
    s += f'Chat used time: {used_time:.2f}s\n'
    s += '-' * 100 + '\n'
    for k, v in kwargs.items():
        s += f'{k}: {v} \t'
    s += '=' * 100 + '\n'

    logger.info(s)

def experi_realworld_malicious(llm:LLM, recover_mode:str, few_shot:bool = False):
    global benchmark_dir
    global samples_json

    model_name = llm.llm_name
    prompt_type = 'few-shot' if few_shot else 'zero-shot'

    results_save_file = os.path.join('results', 'real_world', 'malicious_samples', prompt_type, f'{llm.llm_name}.json')
    
    if os.path.exists(results_save_file):
        with open(results_save_file, 'r') as f:
            results = json.load(f)
    else:
        results = {}

    logger.add(f'logs/real_world/malicious_samples/{prompt_type}/RQ1_{model_name}.log', level='INFO')

    with open(os.path.join(benchmark_dir, samples_json), 'r') as f:
        samples = json.load(f)
    
    try:
        for sample in samples:
            process_flag = False
            if recover_mode == 'True':
                llm_output_result = results.get(str(sample['id']), {}).get(model_name, {}).get('output', '')
                process_flag = llm_output_result.startswith('[ERROR]')
            else:
                process_flag = True

            if process_flag:

                if prompt_type == 'few-shot':
                    messages = build_ICL_prompt_messages(sample['code_without_comment'])
                else:
                    messages = build_prompt_messages(sample['code_without_comment'])
                
                start = time.time()
                result = llm.chat(messages, temperature=0.6, top_p=0.9)
                used_time = round(time.time() - start, 2)
                
                print_results(sample['id'], result, used_time)
                
                results[sample['id']] = {}
                results[sample['id']][model_name] = {}
                results[sample['id']][model_name]['output'] = result
                results[sample['id']][model_name]['used_time'] = used_time
    except Exception:
        exception_stack = traceback.format_exc()
        print(exception_stack)
        logger.exception(exception_stack)
    
    with open(results_save_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

def experi_realworld_benign(llm:LLM, recover_mode:str, few_shot:bool = False):
    global benchmark_dir
    global benign_info_json
    
    model_name = llm.llm_name
    prompt_type = 'few-shot' if few_shot else 'zero-shot'

    results_save_file = os.path.join('results', 'real_world', 'benign_samples', prompt_type, f'{llm.llm_name}.json')

    if os.path.exists(results_save_file):
        with open(results_save_file, 'r') as f:
            results = json.load(f)
    else:
        results = {}

    logger.add(f'logs/real_world/benign_samples/{prompt_type}/RQ2_{model_name}.log', level='INFO')

    with open(os.path.join(benchmark_dir, benign_info_json), 'r') as f:
        benign_samples = json.load(f)

    try:
        for sample in benign_samples:
            process_flag = False
            if recover_mode == 'True':
                llm_output_result = results.get(str(sample['id']), {}).get(model_name, {}).get('output', '')
                process_flag = llm_output_result.startswith('[ERROR]')
            else:
                process_flag = True

            if process_flag:

                with open(os.path.join(benchmark_dir, sample['filepath']), 'r') as f:
                    code = f.read()

                if prompt_type == 'few-shot':
                    messages = build_ICL_prompt_messages(code)
                else:
                    messages = build_prompt_messages(code)
                
                start = time.time()
                result = llm.chat(messages, temperature=0.6, top_p=0.9)
                used_time = round(time.time() - start, 2)
                
                print_results(sample['id'], result, used_time)
                
                results[sample['id']] = {}
                results[sample['id']][model_name] = {}
                results[sample['id']][model_name]['output'] = result
                results[sample['id']][model_name]['used_time'] = used_time
                results[sample['id']][model_name]['obfuscation_level'] = sample['obfuscation_level']
                results[sample['id']][model_name]['category'] = sample['category']
        
    except Exception:
        exception_stack = traceback.format_exc()
        print(exception_stack)
        logger.exception(exception_stack)
    
    with open(results_save_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def experi_obfuscation(llm:LLM, recover_mode:str, few_shot:bool = False):
    global benchmark_dir
    obfuscate_info_json = 'obfuscated_samples_info.json'
    
    model_name = llm.llm_name
    prompt_type = 'few-shot' if few_shot else 'zero-shot'

    results_save_file = os.path.join('results', 'obfuscation', prompt_type, f'{llm.llm_name}.json')

    try:
        with open(results_save_file, 'r') as f:
            results = json.load(f)
    except:
        results = {}

    logger.add(f'logs/obfuscation/{prompt_type}/RQ3_{model_name}.log', level='INFO')

    with open(os.path.join(benchmark_dir, obfuscate_info_json), 'r') as f:
        benign_samples = json.load(f)

    try:
        for sample in benign_samples:
            process_flag = False
            if recover_mode == 'True':
                llm_output_result = results.get(str(sample['id']), {}).get(model_name, {}).get('output', '')
                process_flag = llm_output_result.startswith('[ERROR]')
            else:
                process_flag = True

            if process_flag:
                with open(os.path.join(benchmark_dir, sample['filepath']), 'r') as f:
                    code = f.read()

                messages = build_prompt_messages(code)
                
                start = time.time()
                result = llm.chat(messages, temperature=0.6, top_p=0.9)
                used_time = round(time.time() - start, 2)
                
                print_results(sample['id'], result, used_time, category=sample.get('category', 'N/A'), obfuscation_level=sample.get('obfuscation_level', 'N/A'))
                
                results[sample['id']] = {}
                results[sample['id']][model_name] = {}
                results[sample['id']][model_name]['output'] = result
                results[sample['id']][model_name]['used_time'] = used_time
        
    except Exception:
        exception_stack = traceback.format_exc()
        print(exception_stack)
        logger.exception(exception_stack)
    
    with open(results_save_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

def experi_codemixture(llm:LLM, recover_mode:str, few_shot:bool = False):
    global benchmark_dir
    inject_sample_json = 'inject_samples_info.json'

    model_name = llm.llm_name
    prompt_type = 'few-shot' if few_shot else 'zero-shot'

    results_save_file = os.path.join('results', 'codemixture', prompt_type, f'{llm.llm_name}.json')

    try:
        with open(results_save_file, 'r') as f:
            results = json.load(f)
    except:
        results = {}

    logger.add(f'logs/codemixture/{prompt_type}/RQ4_{model_name}.log', level='INFO')

    with open(os.path.join(benchmark_dir, inject_sample_json), 'r') as f:
        benign_samples = json.load(f)

    try:
        for sample in benign_samples:
            process_flag = False
            if recover_mode == 'True':
                llm_output_result = results.get(str(sample['id']), {}).get(model_name, {}).get('output', '')
                process_flag = llm_output_result.startswith('[ERROR]')
            else:
                process_flag = True

            if process_flag:
                with open(os.path.join(benchmark_dir, sample['filepath']), 'r') as f:
                    code = f.read()

                messages = build_prompt_messages(code)
                
                start = time.time()
                result = llm.chat(messages, temperature=0.6, top_p=0.9)
                used_time = round(time.time() - start, 2)
                
                print_results(sample['id'], result, used_time, inject_type=sample.get('inject_type', 'N/A'))
                
                results[sample['id']] = {}
                results[sample['id']][model_name] = {}
                results[sample['id']][model_name]['output'] = result
                results[sample['id']][model_name]['used_time'] = used_time
        
    except Exception:
        exception_stack = traceback.format_exc()
        print(exception_stack)
        logger.exception(exception_stack)
    
    with open(results_save_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Run evaluation RQs for different LLMs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("--RQ", type=str, required=True, choices=['realworld_malicious', 'realworld_benign', 'obfuscation', 'codemixture'], help="Run which RQs? ")
    parser.add_argument("--model", type=str, required=True, help="Model name or local path.")
    parser.add_argument("--recmode", type=str, required=True, choices=['True', 'False'], help="Run which RQs? ")
    parser.add_argument("--few-shot", type=str, required=True, choices=['True', 'False'], help="Whether to use few-shot learning mode. ")

    args = parser.parse_args()
    
    if args.model in DEEPSEEK_ALLOWED_LLM_LIST:
        # NOTE: Use DeepSeek
        llm = DeepSeek(args.model)
    elif args.model in QWEN_ALLOWED_LLM_LIST:
        # NOTE：Use QWen Model
        llm = Qwen(args.model)
    elif args.model in LLAMA_ALLOWED_LLM_LIST:

        # NOTE: Use Llama Model(Llama2、Llama3)
        llm = Llama(args.model)

    if args.RQ == 'realworld_malicious':
        experi_realworld_malicious(llm, args.recmode, few_shot=(args.few_shot=='True'))
    elif args.RQ == 'realworld_benign':
        experi_realworld_benign(llm, args.recmode, few_shot=(args.few_shot=='True'))
    elif args.RQ == 'obfuscation':
        experi_obfuscation(llm, args.recmode, few_shot=(args.few_shot=='True'))
    else:
        experi_codemixture(llm, args.recmode, few_shot=(args.few_shot=='True'))

if __name__ == '__main__':
    main()
