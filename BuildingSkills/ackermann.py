def ack(m, n):
	'''
	Evaluates the Ackermann function
	'''
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return ack(m-1, 1)
	if m > 0 and n > 0:
		x = ack(m, n-1)
		return ack(m-1, x)

print ack(3, 5)