import math

def hypotenuse(a, b):
	'''
	Returns the length of the hypotenuse of a right
	triangle given the lengths of the two sides as 
	arguments.
	'''
	csquare = a**2 + b**2
	return math.sqrt(csquare)

print hypotenuse(3, 4)