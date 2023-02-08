# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

values = sys.argv[1:]
#print(values)
sum = 0
for flt in values:
	sum += float(flt)*math.log2(1/float(flt))
print("%0.3f" % sum)


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
