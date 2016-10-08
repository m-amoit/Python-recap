def z_fill(i, len):
	'''Return integer i written as a string with at 
	least (len) digits'''
	return str(i).zfill(len)

def reverse(i, j):
	'''Check whether the given figurse are the 
	reverse of each other'''
	return z_fill(i, 2) == z_fill(j, 2)[::-1]

def is_reversed(daughter):
	'''Checks for reverse values of simultaneous 
	mother daughter ages. (Only works when the age
	difference is a multiple of nine)
	'''
	diff = 36
	mother = daughter + diff
	if reverse(daughter, mother):
		print daughter, mother
	else:
		is_reversed(daughter+1)

print is_reversed(0)