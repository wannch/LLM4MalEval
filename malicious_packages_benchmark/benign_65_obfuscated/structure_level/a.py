from collections import Counter
import re
from pathlib import Path

def top_word_counts(filepath, top_n=20):
    text = Path(filepath).read_text(encoding='utf-8', errors='ignore')
    words = re.findall("\\b[a-zA-Z']+\\b", text.lower())
    if False:
        _var_150_0 = (806, 298, 793)
        _var_150_1 = (692, 136, 806)

        def _var_150_fn():
            pass
    counts = Counter(words)
    return counts.most_common(top_n)
if False:
    _var_151_0 = (193, 856, 856)
    _var_151_1 = (29, 932, 674)

    def _var_151_fn():
        pass
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Show top N words in a text file')
    parser.add_argument('file', help='Path to text file')
    parser.add_argument('--top', type=int, default=20, help='How many top words to show')
    args = parser.parse_args()
    for (word, cnt) in top_word_counts(args.file, args.top):
        print(f'{word:20} {cnt}')