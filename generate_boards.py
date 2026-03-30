import os

output_dir = "boards"
os.makedirs(output_dir, exist_ok=True)

# 10 steps from 0.05 to 0.005
thicknesses = [0.05 - i * (0.045 / 9) for i in range(10)]

for i, t in enumerate(thicknesses):
    filename = os.path.join(output_dir, f"board_{i+1:02d}_t{t:.3f}.obj")
    z = t / 2.0
    
    with open(filename, 'w') as f:
        f.write("# OBJ file\n")
        f.write(f"# Thickness: {t:.3f}\n")
        # Vertices
        f.write(f"v -1.0 -1.0 {-z:.4f}\n")
        f.write(f"v  1.0 -1.0 {-z:.4f}\n")
        f.write(f"v  1.0  1.0 {-z:.4f}\n")
        f.write(f"v -1.0  1.0 {-z:.4f}\n")
        f.write(f"v -1.0 -1.0 {z:.4f}\n")
        f.write(f"v  1.0 -1.0 {z:.4f}\n")
        f.write(f"v  1.0  1.0 {z:.4f}\n")
        f.write(f"v -1.0  1.0 {z:.4f}\n")
        
        # Faces (Triangles)
        # Bottom
        f.write("f 4 3 2\n")
        f.write("f 4 2 1\n")
        # Top
        f.write("f 5 6 7\n")
        f.write("f 5 7 8\n")
        # Front
        f.write("f 8 7 3\n")
        f.write("f 8 3 4\n")
        # Back
        f.write("f 1 2 6\n")
        f.write("f 1 6 5\n")
        # Right
        f.write("f 2 3 7\n")
        f.write("f 2 7 6\n")
        # Left
        f.write("f 4 8 5\n")
        f.write("f 4 5 1\n")

print(f"Generated 10 obj files in {os.path.abspath(output_dir)}")
