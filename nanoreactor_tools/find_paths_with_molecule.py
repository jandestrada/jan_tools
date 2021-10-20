



def get_reactants_and_products(reaction_label):
    # a reaction label is a string given from the nanoreactor, and has the shape A + B => C + D
    # TODO: Function not done
    r, p = reaction_label.split("=>")
    



def remove_reaction_tag(reaction_label):
    # gets rid of that initial "    <present>" part of the tag
    
    split_label = reaction_label.split()
    return " ".join(split_label[1:])


def get_present_reactions_from_file(fp):
    # returns a list of reactions with the tag 'present' from a output_monitor.txt file
    monitor_file = open(fp).read().splitlines()
    present_reactions = [remove_reaction_tag(line) for line in monitor_file if "<present>" in line and "=>" in line]

    
#    print(present_reactions)

    return present_reactions

def get_reactions_with_target_molecule(present_reactions, target_molecule):
    return [rxn for rxn in present_reactions if target_molecule in rxn]
    



if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    target_molecule_smi = sys.argv[2]
    present_reactions = get_present_reactions_from_file(file_path)
    [print(l+"\n") for l in get_reactions_with_target_molecule(present_reactions, target_molecule_smi)]


