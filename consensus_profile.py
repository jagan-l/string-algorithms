""" 
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""


def parse_fasta(file_path):
    sequences = [] #to store all the sequences 
    current_seq = "" # to build the current sequences
    
    with open(file_path) as f:
        for line in f:
            line = line.strip() #remove spaces & \n
            
            if line.startswith(">"): #checking if the  line is header
                if current_seq: #if already built a sequeces(if its not empty) we'll add to the list
                    sequences.append(current_seq)
                    current_seq = "" #reset current_ to start new seqeunces
            else:
                current_seq += line # if its not a header, we'll append the lind to current seq
        if current_seq:
            sequences.append(current_seq) #after the loop if we still have one sequence left so we add it manually
    return sequences

#biulding a matrix profile
def build_profile_matrix(sequences):
    length = len(sequences[0]) # since all the seqeunces are of same length so we take a length of first string to know how many column
    profile = { #intialize key with A,C,G,T * values are list of zeores
        'A' : [0] * length,
        'C' : [0] * length,
        'G' : [0] * length,
        'T' : [0] * length
    }
    
    for seq in sequences:
        for i, base in enumerate(seq): 
            profile[base][i] += 1
    
    return profile

def get_consensus(profile):
    consenses = "" 
    length = len(profile['A'])
    for i in range(length):
        max_count = -1 #keep track of height count at position i
        max_base = ''
        
        for base in 'ACGT': #loop through each base in a column 
            count = profile[base][i] #get how many bases appreared at position i
            if count > max_count:
                max_count = count
                max_base = base
        consenses += max_base
            
    return consenses

                
sequences = parse_fasta("dna_sequences.fasta")  
profile = build_profile_matrix(sequences)
consensus = get_consensus(profile)

print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(str(x) for x in profile[base])}")   