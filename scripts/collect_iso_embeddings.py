import json
import os
import sys

def collect_embeddings(input_dir, output_path):
    embeddings = []

    for filename in sorted(os.listdir(input_dir)):
        if not filename.lower().endswith(".json"):
            continue

        full_path = os.path.join(input_dir, filename)

        try:
            with open(full_path, "r") as f:
                data = json.load(f)

            # Extract the embedding from results → embedding
            emb = data["results"]["embedding"]
            embeddings.append(emb)

        except Exception as e:
            print(f"Skipping {filename}: {e}")

    # Save as a simple list-of-lists
    with open(output_path, "w") as f:
        json.dump(embeddings, f)

    print(f"Collected {len(embeddings)} embeddings → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python collect_iso_embeddings.py <input_dir> <output_json>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_json = sys.argv[2]

    collect_embeddings(input_dir, output_json)
