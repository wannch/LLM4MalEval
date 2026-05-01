import json
import os
from typing import Dict, List, Tuple

DIMENSIONS = [
    "LLM_REASON_CONSISTENT",
    "LLM_REASON_CONSISTENT_WITH_CODE",
    "VALID_RESPONSE",
    "EXPLICIT_RESPONSE",
    "LLM_MALICIOUS_RESULT"
]

def process_file(filepath: str) -> Tuple[int, int, Dict[str, int]]:
    """
    Process a single JSON file and return:
    - total_samples: int
    - correct_samples: int (samples where value == 'y')
    - dimension_errors: Dict[str, int] (count of samples where each dimension is incorrect)
    """
    with open(filepath, 'r') as f:
        data = json.load(f)

    total_samples = len(data)
    correct_samples = 0
    dimension_errors = {dim: 0 for dim in DIMENSIONS}

    for key, value in data.items():
        if value == 'y':
            correct_samples += 1
        elif isinstance(value, list):
            for error_dim in value:
                if error_dim in dimension_errors:
                    dimension_errors[error_dim] += 1
        else:
            # Unexpected value, but for now, treat as all errors
            for dim in DIMENSIONS:
                dimension_errors[dim] += 1

    return total_samples, correct_samples, dimension_errors

def calculate_accuracies(directory: str) -> Tuple[Dict[str, float], float, Dict[str, float]]:
    """
    Calculate accuracies for all JSON files in the directory.

    Returns:
    - per_file_accuracy: Dict[str, float] (filename -> accuracy)
    - overall_accuracy: float
    - dimension_accuracies: Dict[str, float] (dimension -> accuracy)
    """
    all_files = [f for f in os.listdir(directory) if f.endswith('.json') and 'CodeLlama-70b' not in f]

    per_file_accuracy = {}
    total_samples_overall = 0
    correct_samples_overall = 0
    dimension_errors_overall = {dim: 0 for dim in DIMENSIONS}

    for filename in all_files:
        filepath = os.path.join(directory, filename)
        total, correct, dim_errors = process_file(filepath)

        if total > 0:
            accuracy = correct / total
            per_file_accuracy[filename] = accuracy
        else:
            per_file_accuracy[filename] = 0.0

        total_samples_overall += total
        correct_samples_overall += correct

        for dim, count in dim_errors.items():
            dimension_errors_overall[dim] += count

    overall_accuracy = correct_samples_overall / total_samples_overall if total_samples_overall > 0 else 0.0

    dimension_accuracies = {}
    for dim in DIMENSIONS:
        # Accuracy for dimension: total_samples - errors for that dimension
        dim_correct = total_samples_overall - dimension_errors_overall[dim]
        dimension_accuracies[dim] = dim_correct / total_samples_overall if total_samples_overall > 0 else 0.0

    return per_file_accuracy, overall_accuracy, dimension_accuracies

def print_statistics(directory: str) -> None:
    """
    Print the statistics for the JSON files in the directory.
    """
    per_file_acc, overall_acc, dim_acc = calculate_accuracies(directory)

    print("Accuracy of each JSON file:")
    for filename, acc in per_file_acc.items():
        print(f"  {filename}: {acc:.4f}")

    print(f"\nOverall accuracy of all JSON files: {overall_acc:.4f}")

    print("\nAccuracy of each dimension:")
    for dim, acc in dim_acc.items():
        print(f"  {dim}: {acc:.4f}")

if __name__ == "__main__":
    directory = "results_annotation/mannual_verify_GPT52_label"
    print_statistics(directory)
