#!/home/jdep/.conda/envs/rp/bin/python
from pathlib import Path
import sys
import shutil
from functions import *
import os


data_dir = Path(sys.argv[1]) # folder that contains subfolders called geodesic_results_x or geodesic_results

#try: # if we just want to calculate the energy of some of the folders
#    start_index = sys.argv[2]
#    end_index = sys.argv[3]

# all the subdirectories in data_dir
subdirs = [x for x in data_dir.iterdir() if x.is_dir()]
subdirs = [s for s in subdirs if "geodesic" in s.stem]

# iterate through each of these and submit a terachem job for this
for sd in subdirs:
    print(sd)
    # split the trajectory into frames
    split_multiple_xyz( sd / "output_geodesic.xyz" )
    
    
    # directory containing all frames files that we want to compute energy from
    frames_sd = sd / "output_geodesic_files" 

    # get each frame
    all_frames = [f for f in frames_sd.iterdir() if "xyz" in f.suffix]
    
    #print(all_frames) 
    
    for frame in all_frames:
        # make a subdir for computing this frame's energy
        frame_sd = frame.parent / (frame.stem + "_tc")
        if not frame_sd.is_dir():
            frame_sd.mkdir()
       # shutil.copy("/home/jdep/templates/traj_energies/tc.in", frame_sd)
        shutil.copy(frame, frame_sd / "structure.xyz")
        shutil.copy("/home/jdep/scripts/bash_helpers/run_tc_opt.sh", frame_sd)

        # get cwd so that I can move back here after submitting
        cwd = os.getcwd()

        os.chdir(frame_sd)

       # print("going to run this file:", frame_sd/"run_tc.sh")
        os.system("sbatch ./run_tc_opt.sh")

        os.system('sleep 1')
        
        
        os.chdir(cwd)
