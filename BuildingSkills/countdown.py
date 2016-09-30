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

print_n('Go home', 7)