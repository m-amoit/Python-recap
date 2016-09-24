def fermat(a, b, c, n):
	'''
	A function that checks whether Fermat's theorem 
	holds.
	Fermat's Theorem states that there are no positive 
	integers a, b, c such that for any values of n 
	greater than 2:
	 a**n + b**n = c**n
	'''
	if a**n + b**n == c**n:
		return 'Holy smokes, Fermat was wrong!'
	else:
		return "No, that doesn't hold"

x = int(raw_input('Enter positive integer a '))
y = int(raw_input('Input integer b '))
z = int(raw_input('Input integer c '))
en = int(raw_input('What is n? '))

print fermat(x, y, z, en)
