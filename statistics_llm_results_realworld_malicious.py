import json
import csv
import os
from collections import defaultdict

def load_sample_types(sample_file_path):
    """Load sample IDs and their malicious types from the sample file."""
    with open(sample_file_path, 'r', encoding='utf-8') as f:
        samples = json.load(f)
    id_to_types = {}
    for sample in samples:
        id_to_types[str(sample['id'])] = sample['mal_type'] if isinstance(sample['mal_type'], list) else [sample['mal_type']]
    return id_to_types

def load_llm_results(llm_file_path):
    """Load LLM results from a JSON file."""
    with open(llm_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_llm_results(llm_results_dir, sample_info_file):
    """Analyze all LLM results and compute statistics."""
    # Load sample types
    id_to_types = load_sample_types(sample_info_file)

    # Get all mal_types
    mal_types = set()
    for types_list in id_to_types.values():
        for t in types_list:
            mal_types.add(t)

    # Dimensions
    dimensions = [
        'LLM_REASON_CONSISTENT',
        'LLM_REASON_CONSISTENT_WITH_CODE',
        'VALID_RESPONSE',
        'EXPLICIT_RESPONSE',
        'LLM_MALICIOUS_RESULT'
    ]

    # Structure to hold counts: llm -> mal_type -> dimension -> count
    stats = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    total_stats = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    # Process each LLM file
    for filename in os.listdir(llm_results_dir):
        if filename.endswith('.json'):
            llm_name = filename.replace('gpt_label_RQ1_', '').replace('.json', '')
            llm_file_path = os.path.join(llm_results_dir, filename)
            llm_results = load_llm_results(llm_file_path)

            for sample_id, result in llm_results.items():
                if sample_id not in id_to_types:
                    continue  # Skip if sample not in types
                mal_types_list = id_to_types[sample_id]

                # Count per mal_type
                for mal_type in mal_types_list:
                    for dim in dimensions:
                        try:
                            if result.get(dim) == 'y':
                                stats[llm_name][mal_type][dim] += 1
                        except AttributeError:
                            print(f'Error file: {llm_file_path}, sample_id: {sample_id}')
                            exit(1) 
                        total_stats[llm_name][mal_type][dim] += 1

                # Count total (once per sample)
                for dim in dimensions:
                    if result.get(dim) == 'y':
                        stats[llm_name]['total'][dim] += 1
                    total_stats[llm_name]['total'][dim] += 1

    return stats, total_stats, mal_types, dimensions

def write_csv(stats, total_stats, mal_types, dimensions, output_file):
    """Write statistics to CSV file."""
    # Prepare header
    header = ['LLM']
    for mal_type in sorted(mal_types):
        for dim in dimensions:
            header.append(f'{mal_type}_{dim}')
    for dim in dimensions:
        header.append(f'total_{dim}')

    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for llm in sorted(stats.keys()):
            row = [llm]
            for mal_type in sorted(mal_types):
                for dim in dimensions:
                    count = stats[llm][mal_type][dim]
                    total = total_stats[llm][mal_type][dim]
                    # row.append(f"{count}/{total}")
                    row.append(f"{count/total * 100: .2f}" if total > 0 else "N/A")
            for dim in dimensions:
                count = stats[llm]['total'][dim]
                total = total_stats[llm]['total'][dim]
                # row.append(f"{count}/{total}")
                row.append(f"{count/total * 100: .2f}" if total > 0 else "N/A")

            writer.writerow(row)

def main():
    llm_results_dir = 'results_annotation/real_world/malicious_samples/few_shot'
    sample_info_file = 'malicious_packages_benchmark/benign_code_info.json'
    output_file = 'results_evaluate_metric/realworld_malicious_few_shot_llm_results_statistics.csv'

    stats, total_stats, mal_types, dimensions = analyze_llm_results(llm_results_dir, sample_info_file)
    write_csv(stats, total_stats, mal_types, dimensions, output_file)
    print(f"Statistics written to {output_file}")

if __name__ == '__main__':
    main()
