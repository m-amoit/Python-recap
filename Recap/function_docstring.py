def print_max(x, y):
	'''Prints the maximum of two values.
	The two values must be integers.'''
	x = int(x)
	y = int(y)
	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

print_max(4, 5)

print print_max.__doc__