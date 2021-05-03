import os
import re

os.chdir(r'C:\Users\pc\Documents\Uni\Level 6\Final Project\Bacterial Efflux Pumps Bioinformatics Investigations\Proteomes\Bacteria_2Do_Proteome\Bacteria_2Do_Proteome_Data\Saprospira_grandis\AcrB-RND-w15-nm3')


with open('fimo.gff', 'r') as a:
    b = a.read()

Protein_ID = re.compile(r'''
    ^WP_[0-9]+\.[0-9]
        ''', re.VERBOSE | re.M)

# NOTE: Takes the Accession number of each protein in the external file and
# NOTE: puts them in a lsit, while removing dupicates
IDs = Protein_ID.findall(b)
ListIDs = list(match for match in IDs)
TupleIDs = tuple(dict.fromkeys(ListIDs))

with open('Hypo Proteins.txt', 'r') as e:
    f = e.read()
    
# NOTE: Matches all proteins in the hypothetical protein file
Motif_Proteins = re.compile(r'''
    (WP_[0-9]+\.[0-9]).+\n
    (.+)\n
    ''', re.VERBOSE | re.M)

# NOTE: Takes all matched hypothetical proteins and converts them into a dictionary 
PMatches = Motif_Proteins.findall(f)
result = {a: b for a, b in PMatches}

print('\n')
print('Proteins with sequnces over 850 amino acids in lenght:')

# NOTE: Matches the acession number of proteins found by the external sowfare
# NOTE: To their sequnce in the dictonary 
values = list(map(result.get, TupleIDs))

# NOTE: Prints the proteins found by the external sofware in a text file
with open('Valid External Proteins.txt', 'w') as g:
    P = []
    for b in values:
        if len(b) >= 850:
            P.append(b)
    for x in P:
        keys = [k for k, v in result.items() if v == x]
        print(*keys, sep='')
        print(keys, x, file=g)
        print('\n', file=g)
    print('\n')
