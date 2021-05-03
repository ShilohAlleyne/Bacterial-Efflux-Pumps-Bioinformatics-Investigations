import os
from Proteome_Toolkit import Type_2_Search

os.chdir(r'C:\Users\pc\Documents\Uni\Level 6\Final Project\Bacterial Efflux Pumps Bioinformatics Investigations\Proteomes\Bacteria_2Do_Proteome\Gemmatirosa_kalamazoonesis')

with open('Type 1 Motifs.txt') as b:
    Type_1 = b.read()

# NOTE: Example of a called function. Here the function for searching for Type 2 motifs
# NOTE: is being used to search Type 1 containg proteins for said Type 2 motif
Type_2_Search.VEKSSSSF(Type_1)
Type_2_Search.SSSS(Type_1)
Type_2_Search.EKSSSS(Type_1)
Type_2_Search.XXXSSSSX(Type_1)
Type_2_Search.XhXXSSSSXh(Type_1)
Type_2_Search.XXpXpSSSSX(Type_1)
Type_2_Search.XhXpXpSSSSXh(Type_1)
