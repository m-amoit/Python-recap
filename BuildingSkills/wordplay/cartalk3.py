def z_fill(i, len):
	'''Return integer i written as a string with at 
	least (len) digits'''
	return str(i).zfill(len)

def reverse(i, j):
	'''Check whether the given figurse are the 
	reverse of each other'''
	return z_fill(i, 2) == z_fill(j, 2)[::-1]

def is_reversed(diff):
	'''Checks for pallindromic mother daughter ages
	and prints the number of times it happens in a 
	mother's lifetime.'''
	count = 0
	daughter = 0
	while True:
		mother = daughter + diff
		if reverse(daughter, mother):
			count += 1
		if mother == 120: break
		daughter += 1
	return count

def check_diff(diff=0):
	'''Check the age differences with pallindromic
	mother daughter ages'''
	x = is_reversed(diff)
	if diff == 70:
		return
	if x > 0:
		print diff, x
	check_diff(diff+1)

check_diff()