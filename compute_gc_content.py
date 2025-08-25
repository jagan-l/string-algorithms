'''
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample dataset:

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Output:
Rosalind_0808
60.919540

'''

#open and read the fasta file

with open("dna_sequences.fasta", "r") as file:
    fasta_data = file.readlines()
    
#creating a dictionary and saving the header and sequencing as key pair values    
sequence = {}
lable = ""

for line in fasta_data:
    line = line.strip() #removing empty line and whitespaces
    if line.startswith(">"):
        lable = line[1:] #this will remove the ">" and only take the read header
        sequence[lable] = ""
    else:
        sequence[lable] += line
        
#calcuate gc content        
def gc_content(dna):
    gc_count = 0
    total_length = 0
    
    for base in dna:
        total_length +=1
        if base == 'G' or base == 'C':
            gc_count +=1
    
    gc_percent = (gc_count/ total_length) * 100
    return gc_percent

#finding the sequence with highest gc content 

max_label = ""
max_gc = 0

for label , sequence in sequence.items():
    gc = gc_content(sequence)
    if gc > max_gc:
        max_gc = gc
        max_label = label
        
        
        
print(max_label)
print(max_gc)



