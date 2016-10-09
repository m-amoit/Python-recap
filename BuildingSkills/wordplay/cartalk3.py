def z_fill(i, len):
	'''Return integer i written as a string with at 
	least (len) digits'''
	return str(i).zfill(len)

def reverse(i, j):
	'''Check whether the given figurse are the 
	reverse of each other'''
	return z_fill(i, 2) == z_fill(j, 2)[::-1]

def is_reversed(daughter, diff):
	'''Checks for pallindromic mother daughter ages.
	'''
	mother = daughter + diff
	if mother == 120:
		return
	if reverse(daughter, mother):
		print daughter, mother
	is_reversed(daughter+1, diff)


is_reversed(0, 36)