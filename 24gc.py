# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

gc = 0
for base in dna:
	if base == "G" or base == "C":
		gc += 1
gcpercent = (gc/len(dna))
print("%.2f"%gcpercent)

"""
python3 24gc.py
0.42
"""
