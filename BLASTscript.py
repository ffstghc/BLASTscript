#########################################################################################
## Extract sequence from random two samples created by https://web.expasy.org/randseq/ ##
#########################################################################################
seq1 = "SEQUENCE 200 AA; 22287 MW; CA76AFAD7E9B646F CRC64; RNAAILMLVP FSFGVKDLRA ILGELLRRNI YQKSTEFFHN PKVRMHLRDK PLGMGSHLQD PYGRAGSKDI QIAVISELEV RATICVETFF WIVENAGVLQ DYIKSDAENP DRSEHSVSWK LEATSANGKV AFYRANLPKP YVGTIIGLGQ DGELTSKRAE CNDLQDTASQ KGPEPGLVEA VCFDLIKYSA MVTTTQMLTH"
seq2 = "SEQUENCE 100 AA; 11150 MW; 86E46D87BAFAF057 CRC64; AKYLKNHLET ILSTDRPPFY LNKRGLEPKV SDRIQMEEGV DIAASQSLNQ FASQMNLAYK TVCDLRSVRV FATKIEVILV WGEPRPLDGG AFGITGAHES DYIKSDAENP DRSEHSVSWK LEATSANGKV AFYRANLPKP PLGMGSHLQD PYGRAGSKDI QIAVISELEV RATICVETFF WIVENAGVLQ MVTTTQMLTH"

posSeq = 7  # Position in list where the acids start

# Split string into parts (list) to extract aminoacids starting at "posSeq"
seq1_acids = seq1.split()[posSeq:]
seq2_acids = seq2.split()[posSeq:]

# Merge list elements back to single string
seq1_acids_merged = ''.join(seq1_acids[:])
seq2_acids_merged = ''.join(seq2_acids[:])

################################################
## Input range to compare and comparison mode ##
################################################
n_acids = len(seq1_acids_merged)  # Amount of amino acids
print("\nLength of sequence: ", n_acids)
print("Input starting position for comparison:")
comp_start = int(input())
print("Input ending position for comparison:")
comp_end = int(input())
print("Start set to:", comp_start, "\n" "End set to:", comp_end)
n_acids_interval = range(comp_start, comp_end)  # Interval for search

###########################
## Input comparison mode ##
###########################
print("\nAvailable comparison modes:\n",
      "(1) Search for matching nucleotides / amino acids\n",
      "(2) Search for mutated nucleosides / amino acids\n",
      "(3) Search for specific nucleoside / amino acid sequence\n",
      "Input 1,2 or 3:")
comp_mode = int(input())


##########################################
## Compare sequences and output results ##
##########################################
def find_sim_seq(s1, s2, interval):
    ind_matches = []
    all_matches = []

    for i in interval:
        if s1[i] == s2[i]:  # Compare for match
            ind_matches.append(i)  # Append position to list with all matches
            match = [s1[i], s2[i]]
            position = [match[0][0], str(i), match[1][0]]  # Combine code with position
            match = ''.join(position[:])  # Get rid of whitespace for correct code displaying
            all_matches.append(match)  # Append to list with matching code + position

    amount_matches = len(ind_matches)  # Total amount of matches
    return amount_matches, all_matches


def find_mut_seq(s1, s2, interval):
    ind_mutations = []
    all_mutations = []

    for i in interval:
        if s1[i] != s2[i]:  # Compare for mutations
            ind_mutations.append(i)  # Append position to list with all mutations
            match = [s1[i], s2[i]]
            position = [match[0][0], str(i), match[1][0]]  # Combine code with position
            match = ''.join(position[:])  # Get rid of whitespace for correct code displaying
            all_mutations.append(match)  # Append to list with mutated code + position

    amount_mutations = len(ind_mutations)  # Total amount of mutations
    return amount_mutations, all_mutations


if comp_mode == 1:  # Find sequence matches
    print("Search for matching sequences initiated.\nGenerating results...")
    X = find_sim_seq(seq1_acids_merged, seq2_acids_merged, n_acids_interval)
    print("\nMatches found in the sequence interval:\n", X[1])
    print("\nTotal amount of matches:", X[0])

elif comp_mode == 2:  # Find mutations
    print("Search for mutated sequences initiated.\nGenerating results...")
    X = find_mut_seq(seq1_acids_merged, seq2_acids_merged, n_acids_interval)
    print("\nMutations found in the sequence interval:\n", X[1])
    print("\nTotal amount of mutations:", X[0])

""""  
else: # Find sequence
    ## Coming next...
"""
