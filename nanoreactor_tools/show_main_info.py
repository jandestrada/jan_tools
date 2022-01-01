#!/home/jdep/.conda/envs/my-rdkit-env/bin/python
import sys
from functions import *
fp = sys.argv[1]

[print(f) for f in get_main_info(fp)]

