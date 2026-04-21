
README — Reproducibility Bundle
Overview
This repository provides a minimal, self contained reproducibility bundle for the geometry analysis described in the accompanying white paper and Technical Companion. It includes:
•	Clean embedding vectors for both BASE and ISO probe families
•	Scripts to regenerate PCA → UMAP projections
•	Final 3D coordinate outputs used in the analysis
•	A deterministic workflow that can be executed on any machine with Python 3.10+
The goal is to allow reviewers to fully reconstruct the geometric results without requiring access to the original model or the full OpenClaw pipeline.
________________________________________
Repository Structure
ai-space-reproducibility/
│
├── data/
│   ├── base_vectors_clean.json        # 30 BASE embeddings
│   └── iso_vectors_clean.json         # 50 ISO embeddings (collected from run files)
│
├── outputs/
│   ├── base_coords.csv                # 3D PCA→UMAP projection for BASE
│   └── iso_coords.csv                 # 3D PCA→UMAP projection for ISO
│
├── scripts/
│   ├── extract_vectors.py             # Extracts vectors from matrix-style JSON
│   ├── collect_iso_embeddings.py      # Collects ISO embeddings from run files
│   └── run_projection.py              # Runs PCA→UMAP and saves 3D coordinates
│
└── README.md
________________________________________
Data Files
BASE Vectors
data/base_vectors_clean.json 
A list of 30 embedding vectors (each 768 dimensional), extracted from the BASE probe family.
ISO Vectors
data/iso_vectors_clean.json 
A list of 50 embedding vectors collected from individual OpenClaw run files for SEM ISO 01.
These vectors were reconstructed using:
scripts/collect_iso_embeddings.py
________________________________________
Scripts
1. collect_iso_embeddings.py
Collects embeddings from individual OpenClaw run files.
Usage:
python scripts/collect_iso_embeddings.py <input_dir> <output_json>
Example:
python scripts/collect_iso_embeddings.py C:\AI-GEOMETRY\20_OPENCLAW\runs\SEM-ISO-01 data\iso_vectors_clean.json
________________________________________
2. extract_vectors.py
Extracts vectors from JSON files that contain a "matrix" field (used for BASE).
Usage:
python scripts/extract_vectors.py <input_json> <output_json>
________________________________________
3. run_projection.py
Runs PCA (10 components) followed by UMAP (3 components) and saves the resulting coordinates.
Usage:
python scripts/run_projection.py --input <vectors_json> --output <coords_csv>
Example:
python scripts/run_projection.py --input data\base_vectors_clean.json --output outputs\base_coords.csv
________________________________________
Reproducing the Projections
BASE Projection
python scripts/run_projection.py --input data\base_vectors_clean.json --output outputs\base_coords.csv
ISO Projection
python scripts/run_projection.py --input data\iso_vectors_clean.json --output outputs\iso_coords.csv
Both commands produce a CSV with three columns:
x, y, z
These correspond to the 3D UMAP embedding used in the analysis.
________________________________________
Environment Requirements
•	Python 3.10 or later
•	Packages: 
o	numpy
o	scikit-learn
o	umap-learn
Install dependencies:
pip install numpy scikit-learn umap-learn
All scripts are CPU only and run deterministically due to fixed random seeds.
________________________________________
Expected Outputs
BASE
•	30 points forming three stable attractors
•	Output file: outputs/base_coords.csv
ISO
•	50 points forming a single dense attractor
•	Output file: outputs/iso_coords.csv
These outputs reproduce the geometry presented in the white paper.
________________________________________
License
This reproducibility bundle is released under the license specified in the repository root.
________________________________________
