# these are functions that are useful



def split_multiple_xyz(fp):
    import sys
    from pathlib import Path

    


    files = fp.open().read().splitlines()

    n_atoms = int(files[0])


    structures = []
    for i in range(int(len(files)/(n_atoms+2))):
        structures.append("\n".join(files[i*(n_atoms + 2):i*(n_atoms + 2) + (n_atoms+2)]))


    out_dir = fp.resolve().parent / (fp.resolve().stem + "_files")
    if not out_dir.exists():
        out_dir.mkdir()

    for i in range(len(structures)):
        out_file = out_dir / (f"structure_{i}"+fp.suffix)
        with out_file.open(mode='w+') as f:
            f.write(structures[i])


def calc_energy_file(fp):
    import shutil
    import os

    out_dir = fp.parent / f"out_{fp.stem}"

    if not out_dir.exists(): out_dir.mkdir()



    shutil.copy("/home/jdep/scripts/bash_helpers/run_tc.sh", out_dir) # copy tc.in to where fp is at
    
    
    
    cwd = os.getcwd()
    os.chdir(str(out_dir.resolve()))



def get_energy_tc_file(tc_out_fp):
    final_energy_line = None


    lines = open(str(tc_out_fp.resolve())).read().splitlines()
    #print("LEN OF LINES:", len(lines))
    for l in lines:
        # since it iterates through each one, the last instance of "FINAL ENERGY" will be the correct one
        if "FINAL ENERGY"==l[:12]:
            #print("found it")
            final_energy_line = l

    if final_energy_line == None:
        print("THIS ONE DIDNT WORK:", tc_out_fp.parent)
        return str(tc_out_fp.parent), None
    final_energy = float(final_energy_line.split()[2])
    return str(tc_out_fp.parent), final_energy

    


def get_energies_tc_dir(tc_dir, filename='tc.out'):

    # i assume I"m being fed a folder like: geodesic_results_0/output_geodesic_files
    all_data = []
    # folders containing tc.out files
    tc_dirs = [t for t in tc_dir.iterdir() if t.is_dir()]
    for tc_dir in tc_dirs:
        all_data.append(get_energy_tc_file(tc_dir/ filename))

    return all_data

