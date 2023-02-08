# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import random
import sys
vals = sys.argv[1:]
readlen = int(vals[2])
gensize = int(vals[0])
readnum = int(vals[1])
frags = []
for i in range(1, readnum +1):
	frags.append(random.randint(1, gensize-readlen))
fullfrags = []
for j in frags:
	fullfrags.append([j,j+readlen])
depth = []
for i in range(1,gensize+1):
	reads = 0
	for j in fullfrags:
		if j[0] <= i <= j[1]:
			reads += 1
	depth.append(reads)
#print(depth)
print(min(depth[readlen:-readlen]),
max(depth),
 sum(depth[readlen:-readlen])/len(depth[readlen:-readlen]))


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
