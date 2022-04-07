#!/global/software/Anaconda3/2019.07/bin/python
import sys
from pathlib import Path

fp = Path(sys.argv[1])




files = fp.open().read().splitlines()

n_atoms = int(files[0])


structures = []
for i in range(int(len(files)/(n_atoms+2))):
    structures.append("\n".join(files[i*(n_atoms + 2):i*(n_atoms + 2) + (n_atoms+2)]))


out_dir = fp.resolve().parent / (fp.resolve().stem + "_files")
if not out_dir.exists():
    out_dir.mkdir()

for i in range(len(structures)):
    out_file = out_dir / (f"structure_{i}"+fp.suffix)
    with out_file.open(mode='w+') as f:
        f.write(structures[i])


