import json
import argparse
from sys import exit as sexit
from os import path
parser = argparse.ArgumentParser(description="convert .txt splitted with '\\n' to .json")
parser.add_argument("-i", "--input", type=str, help="input .txt file path")
parser.add_argument("-o", "--output", type=str, help="output .json file path",)
args = parser.parse_args()
if args.input is None:
    print("[ERROR] Input value is not provided!")
    sexit(1)
else:
    in_path = args.input
if args.output is None:
    out_path = in_path.replace('.txt', '.json')
else:
    out_path = args.output
if not path.exists(in_path):
    print(f"[ERROR] Path '{in_path}' doesn't exists!!!")
    sexit(1)
if not in_path.endswith('.txt'):
    print(f"[ERROR] Input file '{in_path}' not a txt file")
    sexit(1)
if not out_path.endswith('.json'):
    print(f"[ERROR] Output file '{out_path}' not a json file")
    sexit(1)
data = [
    line.strip() for line in open(in_path, encoding='utf-8').read().splitlines() if line.strip() != ''
] 
open(out_path, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))
print(f"Saved as {out_path}")
