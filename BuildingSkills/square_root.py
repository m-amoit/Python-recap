import math

def square_root(a):
	'''
	Estimates the square root of a number using 
	Newton's method.
	
	Compares the estimated square root with 
	the value in math.sqrt. Prints a table with 4
	columns: a, estimated square root, math.sqrt
	value, absolute value of the difference 
	between the two estimates
	'''
	x = a/2.0
	epsilon = 0.0000000000001
	while True:
		y = (x + a/x) / 2
		z = abs(y - x)
		b = math.sqrt(a)
		if z < epsilon:
			print a, x, b, z
			break
		x = y

def test_square_root():
	for i in range(1, 10):
		square_root(float(i))

test_square_root()