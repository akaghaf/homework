# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys

days = int(sys.argv[1])
ppl  = int(sys.argv[2])
Pprime = 1
dayslist = []
for i in range(0, ppl):
	dayslist.append(days-i)
for j in dayslist:
	Pprime *= j/days
P = 1-Pprime
print("%.3f" % P)



"""
python3 33birthday.py 365 23
0.571
"""

