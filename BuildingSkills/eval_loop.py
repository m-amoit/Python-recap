def eval_loop():
	'''Prompts the user, takes the resulting input 
	and evaluates it using eval function, and
	prints the result.
	It should continue until the user enters
	'done'.'''
	while True:
		n = raw_input('Enter string: ')
		if n == 'done':
			break
		print eval(n)
	
eval_loop()