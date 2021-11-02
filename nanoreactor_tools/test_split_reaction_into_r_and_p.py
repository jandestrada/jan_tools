#!/usr/bin/python36
from functions import *
rxn = "[H][O]([H])[H]{1,1} + [H][O][C]([O])[O]{-1,1} + [H][O][H]{0,1} => [H][O][C]([O])[O][H]{0,1} + [H][O][H]{0,1} + [H][O][H]{0,1}"

print(get_reactants_and_products(rxn))


