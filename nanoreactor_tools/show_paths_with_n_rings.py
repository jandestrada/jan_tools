#!/home/jdep/.conda/envs/my-rdkit-env/bin/python
import sys
from functions import *

fp = sys.argv[1]
n_cutoff = int(sys.argv[2])

print("n_cutoff:", type(n_cutoff), n_cutoff)


[print(i+"\n") for i in 
    subselect_reactions_by_n_rings(
        get_present_reactions_from_file(fp),
        n=n_cutoff
    )
]
