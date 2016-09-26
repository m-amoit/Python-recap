def factorial(n):
	'''
	Get the factorial of a number (n) by making 
	recursive calls

	3! == 3*2! = 3*2*1! = 3*2*1*0! = 3*2*1*1
	'''
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

print factorial(3)