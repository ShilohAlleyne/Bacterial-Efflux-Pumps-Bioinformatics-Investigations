import re
import os

os.chdir(r'C:\Users\pc\Documents\Uni\Level 6\Final Project\Bacterial Efflux Pumps Bioinformatics Investigations\Proteomes\Bacteria_2Do_Proteome\Bacteroides_thetaiotaomicron')

Proteome = open(
    'GCF_000011065.1_ASM1106v1_protein.faa', 'r')
Proteome_file = Proteome.read()
Proteome.close()
# NOTE: This allows the proteome file to be read natively

Hypo_pattern = re.compile(r'''
    (\>.                          # NOTE: Makes sure matches from the heading
    .+\shypothetical\sprotein\s   # NOTE: Selects for Hypothetical proteins
    .+)\n                         # NOTE: Matches anything after proteins to a \n
    ([^\>]*)                      # NOTE: Matches anything up to but not including >
    ''', re.VERBOSE | re.M)
# NOTE: Locates Hypo Proteins

Seq_blanks = re.compile(r'\W+')
# NOTE: only mathches for word characters, effectively removing newlines

f = open('Hypo Proteins.txt', 'w')
for match in Hypo_pattern.finditer(Proteome_file):
    title, sequence = match.groups()
    title = title.strip()
# NOTE: Removes trailing whitespaces from the title
    sequence = Seq_blanks.sub("", sequence)
# NOTE: Removes any whitespaces in the sequnce
    print(title, file=f)
    print(sequence, file=f)
    print(file=f)
f.close()
# NOTE: Reformats and prints the Hypo Protein so that the sequnce is one line

print('Hypo Protein Number =', len(Hypo_pattern.findall(Proteome_file)))
# NOTE: Counts the number of Hypo proteins

Protein_pattern = re.compile(r'''
    \>.         # NOTE: Protein code indetifier
    .+\n        # NOTE: Literally anything
    [^\>]*      # NOTE: Matches anything up to but not including ">"
    ''', re.VERBOSE | re.M)
# NOTE: This pattern matches for all the proteins in the Proteome

print('Total Protein Number =', len(Protein_pattern.findall(Proteome_file)))
# NOTE: This counts all the proteins in the proteome
