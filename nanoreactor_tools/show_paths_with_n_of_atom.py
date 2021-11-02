#!/usr/bin/python
import sys
from functions import *

fp = sys.argv[1]
n_cutoff = int(sys.argv[2])
atom = sys.argv[3]

print("n_cutoff:", type(n_cutoff), n_cutoff)
print("atom:", type(atom), atom)



[print(i) for i in 
    subselect_reactions_by_n_atoms(
        get_present_reactions_from_file(fp),
        n=n_cutoff,
        atom=atom
    )
]
