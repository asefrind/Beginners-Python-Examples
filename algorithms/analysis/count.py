#!/usr/bin/python
# -*- coding: utf-8 -*-

# Simple algorithm to count
# number of occurrences of (n) = (length of the array, amount of numbers it has) inside the (ar) = (short for array)

# Sudo: Algorithm
# 	each time (n) is found in (ar)
# 	(count) varible in incremented (by 1)

# I've put spaces to separate different 
# stages of algorithms for easy understanding
# however it isn't a good practice

def count(ar, n):
	count = 0    # Defining a variable to store the value we're going to output
			# Because functions dont return values unless we specify it 
	
	for element in ar:
		# More complex condition could be 
		# => (not element != n)
		if element == n:
			count += 1
	
	return count

# Testing
# add your test cases in list below
test_cases = [([1, 1, 2, 3, 5, 8, 13, 21, 1], 1), ("Captain America", "a")]
for test_case in test_cases:
	print("TestCase: {}, {}".format(test_case[0], test_case[1]))
	print("Results: {}\n".format(count(test_case[0], test_case[1])))

# You can add a condition to check weather the output is correct or not
