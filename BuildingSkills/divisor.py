def is_power(a, b):
	'''
	Takes parameters a, b and returns True if a is
	a power of b.
	
	A number, a, is a power of b if it is 
	divisible by b and a/b is a power of b
	'''
	if a % b == 0:
		x = a/b
		if x % b == 0:
			return True
		else:
			return False
	return False

# print is_power(25, 5)

