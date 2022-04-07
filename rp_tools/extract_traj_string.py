#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import os

fp = sys.argv[1]
out = sys.argv[2]
all_lines = open(fp).read().splitlines()

matched_indices = []
for i in range(len(all_lines)):
    line = all_lines[i]
    if "[GEOCONV]"==line:
        matched_indices.append(i)

matched_indices

n_atoms = int(all_lines[2]) # this is from the xyz header file. Need to remember that we need to add 2 to the number
# of atoms because xyz files have two extra lines besides the atom numbers



frames = []
for ind in matched_indices:
    subset = all_lines[ind-(n_atoms+2) : ind]
    
#     print("\n".join(subset))
    frames.append("\n".join(subset))
# print("\n".join(frames))

f= open(os.path.join(f"{out}", "string_trajectory.xyz"),'w+')
f.write("\n".join(frames))


# In[ ]:




