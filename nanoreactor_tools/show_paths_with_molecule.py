#!/home/jdep/.conda/envs/my-rdkit-env/bin/python
from functions import *
import sys
file_path = sys.argv[1]
target_molecule_smi = sys.argv[2]
present_reactions = get_present_reactions_from_file(file_path)
[print(l+"\n") for l in get_reactions_with_target_molecule(present_reactions, target_molecule_smi)]


