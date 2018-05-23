# Solution for Project Euler - Project 1
# --------------------------------------
# Finds the sum of all multiples of 3 and 5 between 1 and 1000

summation = 0

def findSum(container):
	
	global summation
	
	for i in range(0,1000):
		if i % 3 == 0 or i % 5 == 0:
			container += i

	summation = container

	print summation

findSum(summation)
