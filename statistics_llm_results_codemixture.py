import json
import os
import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
RESULTS_DIR = "results_annotation/codemixture/zero_shot"
INJECT_INFO_PATH = "malicious_packages_benchmark/inject_samples_info.json"
OUTPUT_OVERALL = "results_evaluate_metric/codemixture_zero_shot_llm_results_statistics_overall.csv"
OUTPUT_BY_TYPE = "results_evaluate_metric/codemixture_zero_shot_llm_results_statistics_by_inject_type.csv"

# Model name mapping
model_name_map = {
    'CodeLlama-7b-Instruct-hf': 'CodeLlama-7B',
    'CodeLlama-13b-Instruct-hf': 'CodeLlama-13B',
    'CodeLlama-34b-Instruct-hf': 'CodeLlama-34B',
    'CodeLlama-70b-Instruct-hf': 'CodeLlama-70B',
    'Llama-2-7b-chat-hf': 'Llama-2-7B',
    'Llama-2-13b-chat-hf': 'Llama-2-13B',
    'Llama-2-70b-chat-hf': 'Llama-2-70B',
    'Meta-Llama-3-8B-Instruct': 'Llama-3-8B',
    'Meta-Llama-3-70B-Instruct': 'Llama-3-70B',
    'qwen2-7b-instruct': 'Qwen2-7B',
    'qwen2-72b-instruct': 'Qwen2-72B',
    'qwen3-8b': 'Qwen3-8B',
    'qwen3-14b': 'Qwen3-14B',
    'qwen3-32b': 'Qwen3-32B',
    'deepseek-v3': 'DeepSeek-V3',
    'deepseek-r1': 'DeepSeek-R1'
}

# Inject type labels
inject_type_labels = {
    '1': 'Non-split/Head',
    '2': 'Non-split/Middle',
    '3': 'Non-split/End',
    '4': 'Non-split/Func',
    '5': 'Non-split/Class',
    '6': 'Split/Global',
    '7': 'Split/Func'
}

# Dimensions
DIMENSIONS = [
    "LLM_REASON_CONSISTENT",
    "LLM_REASON_CONSISTENT_WITH_CODE",
    "VALID_RESPONSE",
    "EXPLICIT_RESPONSE",
    "LLM_MALICIOUS_RESULT"
]

def load_inject_info():
    with open(INJECT_INFO_PATH, 'r') as f:
        data = json.load(f)
    inject_map = {}
    type_counts = defaultdict(int)
    for sample in data:
        sample_id = str(sample['id'])
        inject_type = sample['inject_type']
        inject_map[sample_id] = inject_type
        type_counts[inject_type] += 1
    return inject_map, type_counts

def extract_model_name(filename):
    # e.g., gpt_label_RQ4_CodeLlama-13b-Instruct-hf.json -> CodeLlama-13b-Instruct-hf
    if filename.startswith('gpt_label_RQ4_') and filename.endswith('.json'):
        model_name = filename[len('gpt_label_RQ4_'):-len('.json')]
    else:
        model_name = filename.replace('.json', '')
    return model_name

def compute_stats(results, total_samples):
    stats = {}
    for dim in DIMENSIONS:
        yes_count = sum(1 for res in results.values() if isinstance(res, dict) and res.get(dim) == 'y')
        percentage = (yes_count / total_samples) * 100 if total_samples > 0 else 0
        stats[dim] = f"{percentage:.2f}"
    return stats

def compute_stats_by_type(results, inject_map):
    type_results = defaultdict(list)
    for sample_id, res in results.items():
        inject_type = inject_map.get(sample_id)
        if inject_type:
            type_results[inject_type].append(res)
    stats_by_type = {}
    for inject_type, res_list in type_results.items():
        total = len(res_list)
        if total > 0:
            stats = {}
            for dim in DIMENSIONS:
                yes_count = sum(1 for res in res_list if isinstance(res, dict) and res.get(dim) == 'y')
                percentage = (yes_count / total) * 100
                stats[dim] = f"{percentage:.2f}"
            stats_by_type[inject_type] = stats
    return stats_by_type

def main():
    # Load inject info
    inject_map, type_counts = load_inject_info()
    total_samples = len(inject_map)

    # Get list of result files
    result_files = [f for f in os.listdir(RESULTS_DIR) if f.endswith('.json')]
    result_files.sort()  # for consistent order

    # Overall stats
    overall_data = []
    by_type_data = defaultdict(list)
    model_inject_n_counts = defaultdict(lambda: defaultdict(int))

    for filename in result_files:
        filepath = os.path.join(RESULTS_DIR, filename)
        with open(filepath, 'r') as f:
            results = json.load(f)
        model_name = extract_model_name(filename)
        stats = compute_stats(results, total_samples)
        row = [model_name] + [stats[dim] for dim in DIMENSIONS]
        overall_data.append(row)

        # By type
        stats_by_type = compute_stats_by_type(results, inject_map)
        for inject_type, stats in stats_by_type.items():
            row_type = [model_name, inject_type] + [stats[dim] for dim in DIMENSIONS]
            by_type_data[inject_type].append(row_type)

        # Count 'n' for LLM_MALICIOUS_RESULT by inject_type
        for sample_id, res in results.items():
            if isinstance(res, dict) and res.get('LLM_MALICIOUS_RESULT') == 'n':
                inject_type = inject_map.get(sample_id)
                if inject_type:
                    model_inject_n_counts[model_name][inject_type] += 1

    # Write overall CSV
    with open(OUTPUT_OVERALL, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Model'] + DIMENSIONS
        writer.writerow(header)
        writer.writerows(overall_data)

    # Write by type CSV
    with open(OUTPUT_BY_TYPE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Model', 'Inject_Type'] + DIMENSIONS
        writer.writerow(header)
        for inject_type in sorted(by_type_data.keys()):
            writer.writerows(by_type_data[inject_type])

    # Create plots directory
    plots_dir = 'rq4_plots'
    os.makedirs(plots_dir, exist_ok=True)

    # Generate plots
    sns.set_style('whitegrid')
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['font.size'] = 10

    for model, inject_counts in model_inject_n_counts.items():
        display_name = model_name_map.get(model, model)
        labels = [inject_type_labels[str(i)] for i in range(1, 8)]
        counts = [inject_counts.get(str(i), 0) for i in range(1, 8)]
        plt.figure(figsize=(4, 3))  # Size suitable for 4 per row in paper
        bars = plt.bar(labels, counts, color='#A8C6E8', edgecolor=None)  # Lighter academic color, no edges
        plt.ylabel('False Negatives (#)', fontsize=8)
        plt.title(f'{display_name}', fontsize=10)
        plt.xticks(rotation=45, ha='right', fontsize=8)
        plt.yticks(range(0, 55, 10), fontsize=8)
        plt.ylim(0, 55)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                     str(count), ha='center', va='bottom', fontsize=6)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, f'{display_name}.pdf'), format='pdf', bbox_inches='tight', dpi=400)
        plt.close()

if __name__ == "__main__":
    main()