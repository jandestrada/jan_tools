#!/usr/bin/python
import sys
from datetime import datetime

filepath = sys.argv[1]

data = open(filepath).read().splitlines()
time_lines = []

for line in data:
    if "Job " in line:
        #print(line)
        time_lines.append(line.split()[5])


print(time_lines)
time_end = time_lines[1]
time_init = time_lines[0]

print(datetime.strptime(time_end,"%H:%M:%S") - datetime.strptime(time_init,"%H:%M:%S"))
