
________________________________________
AI Space — Reproducibility Bundle
Supporting Materials for the AI Space White Paper and Technical Companion
Author: Gary J. Drypen
Version: R1
Date: April 2026
________________________________________
Overview
This repository provides the minimal reproducibility pipeline required to regenerate the PCA projections and geometric structures reported in:
•	AI Space: A Global Geometric Framework for Understanding Model Behavior (White Paper)
•	Technical Companion to the AI Space White Paper
The materials here allow reviewers to independently verify the geometric findings from the SEMBASE01 and SEMISO01 probe suites using a deterministic, model agnostic workflow.
________________________________________
What This Repository Contains
1. Data Extraction & Processing Scripts
Python scripts for:
•	embedding extraction
•	PCA computation
•	2D and 3D scatter plot generation
•	JSON export of PCA coordinates, centroids, and distances
2. Probe Data
Consolidated JSON files containing:
•	embeddings
•	PCA coordinates
•	cluster IDs
•	centroid distances
•	metadata
3. Prompt Sets
Exact prompts used for:
•	SEMBASE01 (semantic variation probes)
•	SEMISO01 (semantic isolation probes)
4. Model Configuration
•	Identifier and configuration details for the Qwen family model used in the experiments
•	Notes on deterministic execution and fixed random seeds
________________________________________
What This Repository Does Not Contain
This reproducibility bundle intentionally excludes the full DP VIS 01 diagnostic tool described in the White Paper.
DP VIS 01 includes components such as:
•	the trajectory engine
•	worldline playback
•	interactive 3D visualization (Holographic Cube)
•	region highlighting and inspection tools
These are implementation level features intended for exploratory analysis, not for formal reproducibility.
The bundle focuses on the core computational steps required to verify the results:
•	embedding extraction
•	PCA projection
•	cluster structure
•	BASE vs ISO comparison
This separation is intentional and aligns with GFJ’s reproducibility guidelines.
________________________________________
Repository Structure
ai-space-reproducibility/
│
├── data/
│   ├── base_vectors_clean.json        # 30 BASE embeddings
│   └── iso_vectors_clean.json         # 50 ISO embeddings
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
A list of 50 embedding vectors collected from individual SEMISO01 run files.
These vectors were reconstructed using:
scripts/collect_iso_embeddings.py
________________________________________
Scripts
1. collect_iso_embeddings.py
Collects embeddings from individual run files.
Usage:
python scripts/collect_iso_embeddings.py <input_dir> <output_json>
Example:
python scripts/collect_iso_embeddings.py C:\AI-GEOMETRY\20_OPENCLAW\runs\SEM-ISO-01 data\iso_vectors_clean.json
________________________________________
2. extract_vectors.py
Extracts vectors from JSON files containing a "matrix" field (used for BASE).
Usage:
python scripts/extract_vectors.py <input_json> <output_json>
________________________________________
3. run_projection.py
Runs PCA (10 components) followed by UMAP (3 components) and saves the resulting coordinates.
Usage:
python scripts/run_projection.py --input <vectors_json> --output <coords_csv>
Examples:
python scripts/run_projection.py --input data/base_vectors_clean.json --output outputs/base_coords.csv
python scripts/run_projection.py --input data/iso_vectors_clean.json --output outputs/iso_coords.csv
________________________________________
Reproducing the PCA Projections
BASE Projection
python scripts/run_projection.py --input data/base_vectors_clean.json --output outputs/base_coords.csv
ISO Projection
python scripts/run_projection.py --input data/iso_vectors_clean.json --output outputs/iso_coords.csv
Both commands produce a CSV with three columns:
x, y, z
These correspond to the 3D UMAP embedding used in the analysis.
________________________________________
Environment Requirements
•	Python 3.10+
•	numpy
•	scikit learn
•	umap learn
•	matplotlib
•	scipy
Install dependencies:
pip install -r requirements.txt
All scripts run deterministically due to fixed random seeds.
________________________________________
Expected Outputs
BASE
•	30 points forming three stable attractors
•	Output: outputs/base_coords.csv
ISO
•	50 points forming a single dense attractor
•	Output: outputs/iso_coords.csv
These outputs reproduce the geometry presented in the White Paper and Technical Companion.
________________________________________
Reproducibility Notes
The experiments were conducted in a deterministic environment with:
•	fixed random seeds
•	a locally hosted Qwen family model
•	no external API calls
•	stable embedding extraction
This ensures that reviewers can reproduce the PCA structures exactly as reported.
________________________________________
License
This reproducibility bundle is released under the MIT License (see LICENSE in the repository root).
________________________________________

