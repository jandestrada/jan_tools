#toms/43.)*(9.5**3))**(1./3))c will use Rui's parameters as scaling base
import sys
import ruamel.yaml
from rdkit import Chem
sys.path.insert(0, "/home/jdep/jan_tools/nanoreactor_tools/functions")
from functions import get_n_atoms_yaml_file


yaml = ruamel.yaml.YAML()

from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq
import random
import os

file_template_fp = sys.argv[1]

##### 
# THIS SECTION WILL CREATE A DICTIONARY OF PARAMETERS FROM A PARAMETER FILE
####


default_parameters = {
            'n_max_molec':20,
            'n_min_molec':10,
            'r1':14,
            'r2':8,
            'k1':0.002,
            'k2':0.005,
            't1':300,
            't2':150,
            'radius_original':5.0,
            'autosize':'yes',
            'nsteps':10000,
            'wait':10,
            'temperature':1000
}
parameters = {}
try:
    parameters_file = open(sys.argv[2],'r').read().splitlines()
    for line in parameters_file:
        keyword, value = line.split() # splits on empty spaces, will look like "r1", "0.003"
        
        
        if keyword not in ['autosize']:
            value = float(value) # make sure the number is not a string
        else:
            value = str(value)
        
        parameters[keyword] = value
        
except: # it means we did not give it a parameters file
    print("WARNING: NO PARAMETERS FILE WAS GIVEN. GOING OFF DEFAULTS")



#####
# THIS SECTION RANDOMLY CREATES A SET OF MOLECULES FROM BASIS OF POSSIBLE MOLECULES
#####

# open yaml file template as a dict
with open(file_template_fp) as file_template:
    file_template_dict = yaml.load(file_template)

print(file_template_dict)


if "radius_original" in parameters.keys():
    file_template_dict["packing"]["dimension"] = parameters['radius_original']
else:
    file_template_dict["packing"]['dimension'] = default_parameters["radius_original"]

if 'autosize' in parameters.keys():
    file_template_dict["packing"]['autosize'] = parameters['autosize']
else:
    file_template_dict['packing']['autosize'] = default_parameters['autosize']

if 'nsteps' in parameters.keys():
    file_template_dict["dynamics"]['nsteps'] = int(parameters['nsteps'])
else:
    file_template_dict["dynamics"]['nsteps'] = default_parameters['nsteps']
if 'wait' in parameters.keys():
    file_template_dict["engine"]["wait"] = int(parameters['wait'])
else:
    file_template_dict["engine"]['wait'] = default_parameters['wait']
if "temperature" in parameters.keys():
    file_template_dict["dynamics"]["T0"] = int(parameters["temperature"])
else:
    file_template_dict["dynamics"]["T0"] = default_parameters["temperature"]


if "force_piston" in parameters.keys():
    # do stuff for piston
    pass
else:
    # make sure to add default for piston shit in dictionary up there
    # also also adjust the dictionary creation step so that the "values" are a list if multiple values are given in .template file
    



#######
# THIS SECTION CALCS THE R1 AND R2 VALUES BASED ON N ATOMS THEN CREATES AN OUTPUT FILE
######


#if os.path.exists(reference_file["species"]["base"]): # check if the 'base' was just a path to an xyz file
    ### TODO: import OBMOL here
    ### load the file to OBMOL
    ### use OBMOL to count how many atoms are in the xyz file and use that as an input to the next section
#    print("idk.")

#else:
n_atoms_in_reference_file = 0
for species in reference_file["species"]['base']:
    if "{" in species:
        species = species.split("{")[0]
#    print(species)
    mol = Chem.MolFromSmiles(species)
    mol = Chem.AddHs(mol)
    n_atoms_in_reference_file += mol.GetNumAtoms()
#       print("SPECIES:", species)
#      print("n_atoms in species:", mol.GetNumAtoms())
n_atoms = n_atoms_in_reference_file



volumetric_keys = ["r1",'r2'] # values that are volumetrically scaled with n_atoms
non_volumetric_keys = ["t1",'t2','k1','k2']


for key in volumetric_keys:
    if key in parameters.keys():
        value = parameters[key]
        file_template_dict['force']['sphere'][key] = (((n_atoms/43.)*(value**3))**(1./3)) 
    else:
        value = default_parameters[key]
        file_template_dict['force']['sphere'][key] = (((n_atoms/43.)*(value**3))**(1./3)) 

for key in non_volumetric_keys:
    if key in parameters.keys():
        value = parameters[key]
        file_template_dict['force']['sphere'][key] = value 
    else:
        value = default_parameters[key]
        file_template_dict['force']['sphere'][key] = value 

# make sure the correct settings are in double quotes
file_template_dict["engine"]["options"]["fon"] = dq("yes")
file_template_dict["engine"]["options"]["levelshift"] = dq("yes")

# output this created version as a file in output directory
output_path = sys.argv[3]


output_file = os.path.join(output_path, "discover.yaml")
yaml.dump(file_template_dict, open(output_file, "w+"))


    

