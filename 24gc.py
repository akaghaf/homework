# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

gc = 0
for base in dna:
	if base == "G" or base == "C":
		gc += 1
print(round(gc/len(dna),2))

"""
python3 24gc.py
0.42
"""
