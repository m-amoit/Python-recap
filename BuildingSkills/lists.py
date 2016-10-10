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

def cumulative(lst):
	'''Takes a list of numbers and returns the 
	cumulative sum; i.e. a new list where the ith 
	element is the sum of the first i + 1 elements 
	from the original list.'''
	x = []
	count = 0
	for i in lst:
		count += i
		x.append(count)
	return x

print cumulative([1, 2, 3])