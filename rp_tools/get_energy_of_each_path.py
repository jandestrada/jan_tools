#!/home/jdep/.conda/envs/rp/bin/python
from pathlib import Path
import os
import sys
from functions import *
import pandas as pd



try:
    mode = sys.argv[2] 
except:
    mode = 'spe' # single point energy


if mode == 'spe':
    filename = 'tc.out'
elif mode == 'opt':
    filename = 'tc_opt.out'
else:
    raise ValueError("Valid modes are: 'spe' and 'opt'")

cwd = Path(sys.argv[1])
dirs = [d for d in cwd.iterdir() if d.is_dir()]

#print(dirs)
all_data = []

for d in dirs:
    path_dir = d / "output_geodesic_files"
    #tc_dir = [x for x in path_dir.iterdir() if x.is_dir()] # all terachem output folders
    print("DOING:", path_dir)
   # print(get_energies_tc_dir(path_dir))
    try:
        all_data += get_energies_tc_dir(path_dir, filename)
    except:
        print("\tFAILED")
        continue

out = cwd / "energies_all_paths.txt"
df_out = pd.DataFrame(all_data, columns=["path", "energy"])
df_out.to_csv(out)


#with out.open("w+") as fout:
#   fout.write("\n".join(all_data))
    
    
