#!/home/jdep/.conda/envs/my-rdkit-env/bin/python
import sys 
from functions import *
fp = sys.argv[1]

[print(i+"\n") for i in get_present_reactions_from_file(fp)]

