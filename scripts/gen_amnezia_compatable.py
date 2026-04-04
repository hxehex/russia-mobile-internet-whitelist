import json
import argparse
from sys import exit as sexit
from os import path
import socket
try:
    from tqdm import tqdm
    TQDM_AVAIBLE = True
except:
    TQDM_AVAIBLE = False

parser = argparse.ArgumentParser(description="convert .json whitelist to amnezia compatable")
parser.add_argument("-i", "--input", type=str, help="input .json file path")
parser.add_argument("-o", "--output", type=str, help="output .json file path",)
args = parser.parse_args()
if args.input is None:
    print("[ERROR] Input value is not provided!")
    sexit(1)
else:
    in_path = args.input
if args.output is None:
    out_path = in_path.replace(".json", '_amnezia.json')
else:
    out_path = args.output

if not path.exists(in_path):
    print(f"[ERROR] Path '{in_path}' doesn't exists!!!")
    sexit(1)
if not in_path.endswith('.json'):
    print(f"[ERROR] Input file '{in_path}' not a json file")
    sexit(1)
if not out_path.endswith('.json'):
    print(f"[ERROR] Output file '{out_path}' not a json file")
    sexit(1)

with open(in_path, encoding='utf-8') as f:
    dump = json.load(f)

out = []

if TQDM_AVAIBLE:
    for row in tqdm(dump, desc="Proccessing", unit="addr"):
        try:
            out.append({
                "hostname": row,
                "ip":  socket.gethostbyname(row)
            })
        except Exception as e:
            print(f"[WARRNING] hostname {row} was skipped becouse of error: '{e}'")
else:
    total = len(dump)
    for i, row in enumerate(dump):
        print(f"Proccesing {round(i/total, 2)}%")
        try:
            out.append({
                "hostname": row,
                "ip":  socket.gethostbyname(row)
            })
        except Exception as e:
            print(f"[WARRNING] hostname {row} name was skipped becouse of error: '{e}'")
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"Saved as {out_path}")