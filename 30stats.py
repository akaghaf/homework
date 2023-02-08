# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

values = sorted(sys.argv[1:])
sum = 0
for val in values:
	sum += int(val)

mean = sum/len(values)

stdsum = 0
for elem in values:
	stdsum += ((int(elem)-mean)**2)
stddev = (stdsum/len(values))**0.5


print("Count:", len(values))
print("Minimum:", "%.1f" % int(min(values)))
print("Maximum:", "%.1f" % int(max(values)))
print("Mean:", "%.3f" % mean)
print("Std. dev:", "%.3f" % stddev)
print("Median:", "%.3f" % int(values[(len(values)//2)]))

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
