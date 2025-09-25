import os
import csv
import trimesh
import numpy as np


# fn for stats extraction
def get_mesh_stats(mesh, filename):
    n_vertices = len(mesh.vertices) # no. of vertices
    n_faces = len(mesh.faces)   #no. of faces
    # bounding box 
    bbox_min = mesh.bounds[0].tolist()
    bbox_max = mesh.bounds[1].tolist()
    return [filename, n_vertices, n_faces, bbox_min, bbox_max]


def normalize_mesh(mesh):
    # moving the center at the origin (0,0,0)
    vert = mesh.vertices - mesh.vertices.mean(axis=0)
    scale = np.max(np.linalg.norm(vert, axis=1))
    # ensures the whole mesh fits inside a unit sphere
    mesh.vertices = vert / scale
    return mesh

# helper fn for handling mesh one at a time
def helper(file_path, output_dir):

    # loading the mesh
    mesh = trimesh.load(file_path, force="mesh")
    
    if mesh is None:
        return None

    filename = os.path.basename(file_path)
    # getting the stats
    stats = get_mesh_stats(mesh, filename)

    # normalizing the mesh
    mesh = normalize_mesh(mesh)

    # saving normalized mesh in .ply
    out_name = filename.replace(".obj", ".ply")
    mesh.export(os.path.join(output_dir, out_name))

    return stats



def main(input_dir="datasets", output_dir="normalized_meshes", csv_file="mesh_stats_1.csv"):

    os.makedirs(output_dir, exist_ok=True)
    all_stats = []
    # passing obj one by one
    for fname in os.listdir(input_dir):
        if fname.endswith(".obj"):
            file_path = os.path.join(input_dir, fname)
            stats = helper(file_path, output_dir)
            if stats:
                all_stats.append(stats)

    # Save everything into a CSV file
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "n_vertices", "n_faces", "bbox_min", "bbox_max"])
        writer.writerows(all_stats)


if __name__ == "__main__":

    main()
