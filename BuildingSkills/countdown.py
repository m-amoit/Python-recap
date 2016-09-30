def countdown(n):
	'''Count down using recursion'''
	if n <= 0:
		print 'Blastoff!'
	else:
		print n
		countdown(n-1)

def print_n(s, n):
	'''Prints a string n times; using recursion'''
	if n <= 0:
		return
	print s
	print_n(s, n-1)

def count_down(n):
	'''Count down using iteration - while statement
	'''
	while n > 0:
		print n
		n -= 1
	print 'Blastoff!'

def printn(s, n):
	'''Print a string n times, using iteration'''
	while n > 0:
		print s
		n -= 1

def break_():
	'''Using break to end a loop'''
	while True:
		line = raw_input('> ')
		if line == 'done':
			break
		print line

	print 'Done!'

break_()

