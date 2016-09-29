def is_power(a, b):
	'''
	Takes parameters a, b and returns True if a is
	a power of b.
	
	A number, a, is a power of b if it is 
	divisible by b and a/b is a power of b
	Base case: power(a, 1) = 2; return True
	'''
	# **Think of the base case**
	if a % b == 0:
		x = a/b
		if x % b == 0:
			return True
		else:
			return False
	return False


def gcd(a, b):
	'''
	Takes parameters a, b and returns their 
	greatest common divisor.

	If r is the remainder when a is divided by b,
	then gcd(a, b) = gcd(b, r). As a base case, we 
	can use gcd(a, 0) = a.
	'''
	if b == 0:
		return a
	r = a % b
	return gcd(b, r)



