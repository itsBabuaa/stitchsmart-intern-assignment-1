# 3D Mesh Preprocessing Script

This script processes 3D mesh files in `.obj` format by:

1. Extracting mesh statistics (number of vertices, faces, and bounding box).
2. Normalizing the mesh to fit inside a unit sphere centered at the origin.
3. Saving the normalized mesh in `.ply` format.
4. Saving all mesh statistics to a CSV file.

---

## Usage (How To Run)

1. Place all your `.obj` mesh files inside the `datasets` folder.
2. Install dependencies via pip:

```bash
pip install trimesh numpy
```

3. Run the script:

```bash
python data_prep.py
```

4. After running:

* Normalized `.ply` meshes will be saved in the `normalized_meshes` folder.
* Mesh statistics will be saved in `mesh_stats.csv`.

## Directory Structure

```
project/
│
├── datasets/              # Input folder containing .obj files
├── normalized_meshes/    # Output folder for normalized .ply files
├── requirements.txt      # list of requirements
├── mesh_stats.csv         # Output CSV with mesh statistics
├── data_prep.py  # This script
├── test-nb.ipynb  # jupyter notebook
└── README.md
```

---

## Optional

You can change the input/output directories and CSV file name by passing arguments to the `main` function in `mesh_preprocessing.py`:

```python
main(input_dir="your_input_folder", output_dir="your_output_folder", csv_file="your_csv_file.csv")
```
