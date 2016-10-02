import math
from factorial import *

def LHS():
	'''The value on the left hand side of the 
	summation'''
	value = (2 * math.sqrt(2))/9801
	return value

def RHS(k):
	'''The value on the right hand side of the 
	summation. 
	num: numerator
	den: denominator'''
	x = 4*k
	num = float(factorial(x) + (1103 + 26390*k))
	den = (factorial(k)**4) * (396**x)
	value = num/den
	return value

def summation(k):
	'''Estimates the value of the summation in the
	equation. Summing the RHS value from k=0 to 
	infinity'''
	summation = 0
	x = RHS(k)
	# summation += x
	while True:
		summation += x
		if x > 1e-15:
			break
		summation(k+1)
	return summation

def estimate_pi():
	'''Estimates the value of pi: inverse value of
	LHS * summation of RHS from k=0 to infinity.'''
	#Estimate the value of 1/pi
	y = LHS() * summation(0)
	pi = 1/y
	return pi

	
print math.pi
print estimate_pi()

