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

############################
## Input range to compare ##
############################
n_acids = len(seq1_acids_merged)  # Amount of amino acids
print("Length of sequence: ", n_acids)
print("Input starting position for comparison:")
comp_start = int(input())
print("Input ending position for comparison:")
comp_end = int(input())
print("Start set to:\n", comp_start, "\n" "End set to:\n", comp_end)

##########################################
## Compare sequences and output results ##
##########################################
n_acids_interval = range(comp_start, comp_end)

ind_hit = []  # Empty for collecting indices of hits
acid_hit = []  # Empty for later collecting acid changes/similarities
all_hits = []  # Empty for collecting all hits

print("Hits found at this positions in the sequence:")
for i in n_acids_interval:
    if seq1_acids_merged[i] == seq2_acids_merged[i]:
        ind_hit.append(i)
        acid_hit = [seq1_acids_merged[i], seq2_acids_merged[i]]  # Collect acids

        pos = [acid_hit[0][0], str(i), acid_hit[1][0]]  # Combine acid locations with position

        hit = ''.join(pos[:])  # Merge hit elements
        all_hits.append(hit)  # Collect all hits
        print(hit)

n_hits = len(ind_hit)  # Total amount of found hits
print("\nTotal amount of hits:", n_hits)