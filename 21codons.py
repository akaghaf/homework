# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for x in range(0,len(dna),3):
	print(dna[x:x+3])

"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
