""" 
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

"""
# read the fasta file
with open ("dna_sequences.fasta") as file:
    lines = file.readlines()

#store only the reads as list in "dna" not the header
dna = "" 
for line in lines:
    if not line.startswith(">"):
        dna += line.strip()
        
#creaing a disctionary for complementory rules
complement = {
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}


def reverse_complement(seq):
    rev_comp= ""
    for base in reversed(seq): #creates an reversed iterater we can loop over.
        rev_comp += complement[base] 
    return rev_comp

for i in range(len(dna)): #i is the start position of substring
    for l in range(4,13): #length 4 to 12 #l is the length of the substring
        if i + l <= len(dna): #to make sure substring doesnt go past end of dna string
            sub = dna[i:i+l]
            if sub == reverse_complement(sub):
                print(i + 1, l)
        
        
    
   