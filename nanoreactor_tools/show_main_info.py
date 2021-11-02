#!/usr/bin/python36
import sys
from functions import *
fp = sys.argv[1]

[print(f) for f in get_main_info(fp)]

