def square_root(a):
	'''
	Takes a as a parameter, chooses a reasonable 
	value of x and uses it to estimate the square
	root of a using Newton's method.
	Epsilon: a small value that determines how 
	close is close enough.'''
	x = a/3.0
	epsilon = 0.00000001
	while True:
		print x
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y

