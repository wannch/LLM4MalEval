import json
import os
import csv

# Load sample information
with open('malicious_packages_benchmark/obfuscated_samples_info.json', 'r') as f:
    sample_info = json.load(f)

id_to_category = {item['id']: item['category'] for item in sample_info}
id_to_obf = {item['id']: item['obfuscation_level'] for item in sample_info}

# Dimensions
dimensions = ['VALID_RESPONSE', 'EXPLICIT_RESPONSE', 'LLM_REASON_CONSISTENT', 'LLM_REASON_CONSISTENT_WITH_CODE', 'LLM_MALICIOUS_RESULT']

# Results directory
results_dir = 'results_annotation/obfuscation/zero_shot/'

# Get all LLM files
llm_files = [f for f in os.listdir(results_dir) if f.endswith('.json')]

# Prepare data for overall CSV
overall_data = []

# Prepare data for obfuscation CSV (aggregated across benign/malicious)
obf_data = []

# Get all possible obfuscation levels
all_obfs = set(id_to_obf.values())

for llm_file in llm_files:
    llm_name = llm_file.replace('gpt_label_RQ3_', '').replace('.json', '')
    with open(os.path.join(results_dir, llm_file), 'r') as f:
        data = json.load(f)

    # Initialize counters for overall
    benign_counts = {dim: 0 for dim in dimensions}
    benign_totals = {dim: 0 for dim in dimensions}
    malicious_counts = {dim: 0 for dim in dimensions}
    malicious_totals = {dim: 0 for dim in dimensions}

    # Initialize counters for obfuscation levels (aggregated)
    obf_totals = {obf: {dim: 0 for dim in dimensions} for obf in all_obfs}
    obf_correct_counts = {obf: {dim: 0 for dim in dimensions} for obf in all_obfs}
    obf_benign_totals = {obf: 0 for obf in all_obfs}
    obf_malicious_totals = {obf: 0 for obf in all_obfs}
    obf_fp = {obf: 0 for obf in all_obfs}  # false positives: benign with 'y'
    obf_fn = {obf: 0 for obf in all_obfs}  # false negatives: malicious with 'n'

    for sample_id_str, result in data.items():
        sample_id = int(sample_id_str)
        if sample_id not in id_to_category:
            continue
        category = id_to_category[sample_id]
        obf = id_to_obf[sample_id]
        is_benign = category == 'benign'

        if not isinstance(result, dict):
            continue  # skip malformed entries

        obf_benign_totals[obf] += 1 if is_benign else 0
        obf_malicious_totals[obf] += 1 if not is_benign else 0

        for dim in dimensions:
            val = result[dim]
            # For overall
            if is_benign:
                benign_totals[dim] += 1
                if val == 'y':
                    benign_counts[dim] += 1
            else:
                malicious_totals[dim] += 1
                if val == 'y':
                    malicious_counts[dim] += 1

            # For obfuscation aggregated
            obf_totals[obf][dim] += 1
            if dim == 'LLM_MALICIOUS_RESULT':
                if is_benign and val == 'y':
                    obf_fp[obf] += 1
                elif not is_benign and val == 'n':
                    obf_fn[obf] += 1
            else:
                # For other dims, 'y' is correct
                if val == 'y':
                    obf_correct_counts[obf][dim] += 1

    # Compute percentages for overall
    benign_pcts = {dim: round((benign_counts[dim] / benign_totals[dim] * 100), 2) if benign_totals[dim] > 0 else 0.0 for dim in dimensions}
    malicious_pcts = {dim: round((malicious_counts[dim] / malicious_totals[dim] * 100), 2) if malicious_totals[dim] > 0 else 0.0 for dim in dimensions}

    # Add to overall data
    overall_data.append({'LLM': llm_name, 'Category': 'benign', **benign_pcts})
    overall_data.append({'LLM': llm_name, 'Category': 'malicious', **malicious_pcts})

    # Compute for each obfuscation level (aggregated)
    obf_row = {'LLM': llm_name}
    for obf in all_obfs:
        for dim in ['VALID_RESPONSE', 'EXPLICIT_RESPONSE', 'LLM_REASON_CONSISTENT', 'LLM_REASON_CONSISTENT_WITH_CODE']:
            pct = round((obf_correct_counts[obf][dim] / obf_totals[obf][dim] * 100), 2) if obf_totals[obf][dim] > 0 else 0.0
            obf_row[f'{dim}_{obf}'] = pct
        # FPR
        fpr_pct = round((obf_fp[obf] / obf_benign_totals[obf] * 100), 2) if obf_benign_totals[obf] > 0 else 0.0
        obf_row[f'FPR_{obf}'] = fpr_pct
        # FNR
        fnr_pct = round((obf_fn[obf] / obf_malicious_totals[obf] * 100), 2) if obf_malicious_totals[obf] > 0 else 0.0
        obf_row[f'FNR_{obf}'] = fnr_pct
    obf_data.append(obf_row)

# Write overall CSV
overall_csv_path = 'results_evaluate_metric/obfuscation_zero_shot_llm_results_statistics_overall.csv'
with open(overall_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['LLM', 'Category'] + dimensions
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in overall_data:
        writer.writerow(row)

# Write obfuscation CSV (aggregated by obfuscation level)
obf_csv_path = 'results_evaluate_metric/obfuscation_zero_shot_llm_results_statistics_by_different_level.csv'
dims_for_obf = ['VALID_RESPONSE', 'EXPLICIT_RESPONSE', 'LLM_REASON_CONSISTENT', 'LLM_REASON_CONSISTENT_WITH_CODE']
fieldnames_obf = ['LLM'] + [f'{dim}_{obf}' for dim in dims_for_obf for obf in sorted(all_obfs)] + [f'FPR_{obf}' for obf in sorted(all_obfs)] + [f'FNR_{obf}' for obf in sorted(all_obfs)]
with open(obf_csv_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames_obf)
    writer.writeheader()
    for row in obf_data:
        writer.writerow(row)

print("Statistics computed and saved to CSV files.")