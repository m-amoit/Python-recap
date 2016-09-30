def square_root(a):
	'''Takes a as a parameter, chooses a reasonable 
	value of x and uses it to estimate the square
	root of a.'''
	x = a/2.0
	while True:
		print x
		y = (x + a/x) / 2
		if y == x:
			break
		x = y

square_root(9)