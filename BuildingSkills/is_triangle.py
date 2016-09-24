def is_triangle(a, b, c):
	'''
	Check whether the given lengths can form a 
	triangle.
	
	If any of the three lengths is greater than 
	the sum of the other two, then you cannot form 
	a triangle. Otherwise you can.
	
	Print 'yes' if you can form a triangle, Otherwise
	print 'yes'.
	'''
	if a > b + c:
		return 'No'
	elif b > a + c:
		return 'No'
	elif c > a + b:
		return 'No'
	return 'Yes'

def get_length():
	a = int(raw_input('Input length 1 \n'))
	b = int(raw_input('Input length 2 \n'))
	c = int(raw_input('Input length 3 \n'))
	return is_triangle(a, b, c)

print get_length()