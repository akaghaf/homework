# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random
bases = 'ATATATCGCG'
string = ""
for x in range(30):
	string += random.choice(bases)
atcontent = 0
for x in string:
	if x == "A" or x == "T":
		atcontent += 1
print(len(string), atcontent/len(string), string)



"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
