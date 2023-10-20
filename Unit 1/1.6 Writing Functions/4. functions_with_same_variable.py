"""Author: Darrien Guan
Date: September 13, 2023
Description: Example of a program that has two functions with the same variable name.
"""

def sum(numOne,numTwo):
	''' This function adds numOne and numTwo together'''
	# using the variable calculation
	calculation = numOne+numTwo
	print(calculation)

def multiply(numOne, numTwo):
	''' This function multiplies numOne and numTwo together'''
	# using the variable calculation
	calculation = numOne*numOne
	print(calculation)

# outputs the value of both functions with the input is 1,1
def main():
	'''mainline logic'''
	print(sum(1,1))
	print(multiply(1,1))