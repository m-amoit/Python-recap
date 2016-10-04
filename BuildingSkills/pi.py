import math
from factorial import *

def estimate_pi():
	'''Estimates the value of pi using the 
	Srinivasa Ramanujan infinite series'''
	total = 0
	k = 0
	factor = 2 * math.sqrt(2)/9801
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		term = factor * num/den
		total += term
		if term <= 1e-15:
			break
		k += 1
	return 1/total

print math.pi
print estimate_pi()

