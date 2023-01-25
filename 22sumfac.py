# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

x = 5
sum = 0
fact= 1
for y in range(1,x+1):
	sum += y
	fact = fact * y
print(x, sum, fact)


"""
python3 22sumfac.py
5 15 120
"""
