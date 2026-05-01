import json
import csv
import os
from collections import defaultdict

def main():
    llm_results_dir = 'results_annotation/real_world/benign_samples/zero_shot'
    output_file = 'results_evaluate_metric/realworld_benign_zero_shot_llm_results_statistics.csv'

    # Dimensions
    dimensions = [
        'LLM_REASON_CONSISTENT',
        'LLM_REASON_CONSISTENT_WITH_CODE',
        'VALID_RESPONSE',
        'EXPLICIT_RESPONSE',
        'LLM_MALICIOUS_RESULT'
    ]

    # Stats: llm -> dimension -> count of 'y'
    stats = {}
    # Totals: llm -> dimension -> total samples (same for all dimensions)
    totals = {}

    # Process each LLM file
    for filename in os.listdir(llm_results_dir):
        if filename.endswith('.json'):
            llm_name = filename.replace('gpt_label_RQ2_', '').replace('.json', '')
            llm_file_path = os.path.join(llm_results_dir, filename)

            with open(llm_file_path, 'r', encoding='utf-8') as f:
                llm_results = json.load(f)

            stats[llm_name] = {}
            totals[llm_name] = {}

            for dim in dimensions:
                stats[llm_name][dim] = 0
                totals[llm_name][dim] = 0

                for sample_id, result in llm_results.items():
                    try:
                        totals[llm_name][dim] += 1
                        if result.get(dim) == 'y':
                            stats[llm_name][dim] += 1
                            
                    except AttributeError as e:
                        print(f"Error in {filename}, sample {sample_id}: {e}, type: {type(result)}")
                        continue
        # Write CSV
    header = ['Model'] + dimensions
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow(header)

        for llm in sorted(stats.keys()):
            row = [llm]

            for dim in dimensions:
                count = stats[llm][dim]
                total = totals[llm][dim]
                percentage = (count / total) * 100 if total > 0 else 0
                row.append(f"{percentage:.2f}")

            writer.writerow(row)

    print(f"Statistics written to {output_file}")

if __name__ == '__main__':
    main()