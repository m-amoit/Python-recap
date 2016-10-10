def nested_sum(lst):
	'''Takes a nested list of integers and adds up 
	the elements in from all of the nested lists.'''
	total = 0
	for i in lst:
		try:
			total += i
		except TypeError:
			total += sum(i)
	return total

def capitalize_nested(lst):
	'''Takes a nested list of strings and returns a 
	new nested list with all strings capitalized.'''
	x = []
	for i in lst:
		try:
			x.append(i.capitalize())
		except AttributeError:
			y = []
			for s in i:
				y.append(s.capitalize())
			x.append(y)
	return x

lst = ['a', 'b', ['c', 'd'],'e', ['f', 'g'],'h']
print capitalize_nested(lst)