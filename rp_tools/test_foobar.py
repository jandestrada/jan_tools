fp =  "/home/jdep/debugging_throwaway_results/terachem_tutorial/tc_LA.out"
from functions import get_energy_tc_file, get_energies_tc_dir
from pathlib import Path

print(get_energy_tc_file(Path(fp)))


dir_fp = "/home/jdep/debugging_throwaway_results/crest_playground/schmidt/crest_files/crest_conformers_files/geodesic_results_0/output_geodesic_files/"
print(get_energies_tc_dir(Path(dir_fp)))


