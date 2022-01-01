#!/home/jdep/.conda/envs/my-rdkit-env/bin/python
import rdkit
from rdkit import Chem
from rdkit.Chem import rdqueries
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')     


def get_reactants_and_products(reaction_label):
    # a reaction label is a string given from the nanoreactor, and has the shape A + B => C + D
    r, p = reaction_label.split("=>")
    
    r_list = [r_i.strip() for r_i in r.split("+")]

    p_list = p.split("+")
    p_list = [p_i.strip() for p_i in p.split("+")]

    r_list = [separate_smiles_and_charge(x, return_smiles=True) for x in r_list]
    p_list = [separate_smiles_and_charge(x, return_smiles=True) for x in p_list]

    #print(r_list)
    #print(p_list)
    return r_list, p_list


def separate_smiles_and_charge(input_info, return_smiles=False):
    smiles, charge_and_eConf = input_info.split("{") # input_info has structure "[H][O][H]{0,1}"
    
    if return_smiles:
        return smiles
    return smiles, "{"+charge_and_eConf


def remove_reaction_tag(reaction_label):
    # gets rid of that initial "    <present>" part of the tag
    
    split_label = reaction_label.split()
    return " ".join(split_label[1:])


def get_present_reactions_from_file(fp):
    # returns a list of reactions with the tag 'present' from a output_monitor.txt file
    monitor_file = open(fp).read().splitlines()
    present_reactions = set([remove_reaction_tag(line) for line in monitor_file if "<present>" in line and "=>" in line])

    
#    print(present_reactions)

    return present_reactions

def get_reactions_with_target_molecule(present_reactions, target_molecule):
    return [rxn for rxn in present_reactions if target_molecule in rxn]
    
def get_main_info(fp):
    # returns a list of the lines of text that only contain "INFO:__main__"
    file = open(fp).read().splitlines()
    return [line for line in file if line[:13]=="INFO:__main__"]




def get_atom_number_from_string(atom_symbol):
    p_table = {
        "C":6,
        "H":1,
        "O":8,
        "N":7
    }    
    return p_table[atom_symbol]

def get_n_atoms_in_a_molecule(smi, atom):


    if not isinstance(atom, str):
        raise TypeError("input needs to be a string")

    # get atom number
    atom_number = get_atom_number_from_string(atom)


    # set up the query
    q = rdqueries.AtomNumEqualsQueryAtom(atom_number)

    # load molecule
    mol = Chem.MolFromSmiles(smi)
    if mol == None:
        print("Smiles:", smi, 'did not work...')
        return 0
#    print(q)
#    print(mol.GetNumAtoms())


    # return the number of atoms that match query in molecule
    return len(mol.GetAtomsMatchingQuery(q))
    
    
    
def get_n_rings_in_a_molecule(smi):
    mol = Chem.MolFromSmiles(smi)
    if mol == None:
        print("Smiles:", smi,"did not work...")
        return 0

    n_rings = mol.GetRingInfo().NumRings()
    return n_rings

def subselect_reactions_by_n_atoms(set_present_reactions, n=2, atom="C"):
    # will return a subset of reactions that contain a molecule that satisfy the condition
    # that it has N number of X atom
    satisfying_rxns = []
    for rxn in set_present_reactions:
        r_list, p_list = get_reactants_and_products(rxn) 

        n_atom_in_r_list = [get_n_atoms_in_a_molecule(molecule, atom) for molecule in r_list]
        n_atom_in_p_list = [get_n_atoms_in_a_molecule(molecule,atom) for molecule in p_list]

        if (n in n_atom_in_r_list) or (n in n_atom_in_p_list):
            satisfying_rxns.append(rxn)

    return satisfying_rxns

def subselect_reactions_by_n_rings(set_present_reactions, n=1):

    satisfying_rxns = []
    for rxn in set_present_reactions:
        r_list, p_list = get_reactants_and_products(rxn) 

        n_rings_in_r_list = [get_n_rings_in_a_molecule(molecule) for molecule in r_list]
        n_rings_in_p_list = [get_n_rings_in_a_molecule(molecule) for molecule in p_list]

        bool_r_list = False
        bool_p_list = False

        for n_reactant in n_rings_in_r_list:
            if n_reactant >= n:
                bool_r_list = True

        for n_product in n_rings_in_p_list:
            if n_product >= n:
                bool_p_list = True
        
        if bool_r_list or bool_p_list:
            satisfying_rxns.append(rxn)
                
            


            satisfying_rxns.append(rxn)

    return satisfying_rxns
