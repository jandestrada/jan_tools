#!/home/jdep/.conda/envs/rp/bin/python

import sys
from pathlib import Path
sys.path.insert(0, "/home/jdep/retropaths/")

from retropaths.abinitio.transformation_3D import *



fp1 = Path(sys.argv[1])
fp2 = Path(sys.argv[2])
try:
    id = sys.argv[3]
except:
    id = None



interpolate_begin_and_end(fp1, fp2, id)
