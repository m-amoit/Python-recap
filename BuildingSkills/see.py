def a(x, y):
	x = x + 1
	return x * y

def b(z):
	prod = a(z, z)
	print z, prod
	return prod

def c(x, y, z):
	total = x + y + z
	square = b(total)**2
	return square

x = 1
y = x + 1
print c(4, 5, 6)