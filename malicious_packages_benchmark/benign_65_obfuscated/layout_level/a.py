import re
from collections import Counter
from pathlib import Path
def top_word_counts(filepath,top_n=20):
  text=Path(filepath).read_text(encoding="utf-8",errors="ignore")
  words=re.findall(r"\b[a-zA-Z']+\b",text.lower())
  counts=Counter(words)
  return counts.most_common(top_n)
if __name__=="__main__":
  import argparse
  parser=argparse.ArgumentParser(description="Show top N words in a text file")
  parser.add_argument("file",help="Path to text file")
  parser.add_argument("--top",type=int,default=20,help="How many top words to show")
  args=parser.parse_args()
  for word,cnt in top_word_counts(args.file,args.top):
    print(f"{word:20} {cnt}")