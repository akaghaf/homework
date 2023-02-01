# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
string = ""
for x in range(1, len(dna)+1):
	string += dna[-x]
complement = ""
for character in string:
	if character == "A"  : complement += "T"
	elif character == "T": complement += "A"
	elif character == "C": complement += "G"
	else                 : complement += "C"
print(complement)


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
