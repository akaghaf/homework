# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import math, sys, mcb185

def entropy(probability):
	assert(math.isclose(1.0, sum(probability)))
	h = 0
	for p in probability:
		if p != 0 : h += (p * math.log2(1/p))
	return h

def seqentropy(seq):
	A = seq.count("A")/len(seq)
	C = seq.count("C")/len(seq)
	G = seq.count("G")/len(seq)
	T = seq.count("T")/len(seq)
	return entropy([A,C,G,T])


framesize = int(sys.argv[2])

for defline, seq in  mcb185.read_fasta(sys.argv[1]):
	print(defline)
	columncounter = 0
	for i in range(len(seq)-framesize+1):
		if seqentropy(seq[i:i+framesize]) < float(sys.argv[3]):
			print("N", end="")
		else: print(seq[i], end="")
		columncounter += 1
		if columncounter % 60 == 0:
			print("\n", end="")

    

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
