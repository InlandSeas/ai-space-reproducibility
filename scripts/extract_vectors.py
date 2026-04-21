import json
import sys
import os

print("RUNNING FILE:", os.path.abspath(__file__))

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, "r") as f:
    data = json.load(f)

vectors = data["matrix"]

with open(output_path, "w") as f:
    json.dump(vectors, f)

print(f"Extracted {len(vectors)} vectors to {output_path}")
