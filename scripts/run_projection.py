import json
import numpy as np
from sklearn.decomposition import PCA
import umap
import csv
import argparse

def load_vectors(path):
    """Load hidden-state vectors from a JSON file."""
    with open(path, "r") as f:
        data = json.load(f)
    return np.array(data)

def run_pca_umap(vectors, pca_components=10, umap_components=3):
    """Run PCA → UMAP on the provided vectors."""
    # PCA first
    pca = PCA(n_components=pca_components)
    reduced = pca.fit_transform(vectors)

    # Then UMAP to 3D
    reducer = umap.UMAP(n_components=umap_components, random_state=42)
    embedding = reducer.fit_transform(reduced)

    return embedding

def save_csv(coords, output_path):
    """Save 3D coordinates to a CSV file."""
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "z"])
        for row in coords:
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Minimal PCA→UMAP projection script.")
    parser.add_argument("--input", required=True, help="Path to JSON file containing vectors.")
    parser.add_argument("--output", required=True, help="Path to output CSV file.")
    args = parser.parse_args()

    print("Loading vectors...")
    vectors = load_vectors(args.input)

    print("Running PCA → UMAP...")
    coords = run_pca_umap(vectors)

    print(f"Saving coordinates to {args.output}...")
    save_csv(coords, args.output)

    print("Done. Projection complete.")

if __name__ == "__main__":
    main()
