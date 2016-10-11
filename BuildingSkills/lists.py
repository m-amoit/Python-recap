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

def middle(lst):
	'''Takes a list and returns a new list that 
	contains all but the first and last elements.'''
	for i in [len(lst) - 1, 0]:
		del lst[i]
	return lst

def chop(lst):
	'''Takes a list, modifies it by removing the 
	first and last elements, and returns None.'''
	for i in [lst[0], lst[len(lst) - 1]]:
		m = lst.remove(i)
	return m

def is_sorted(lst):
	'''Takes a list as a parameter and returns True 
	if the list is sorted in ascending order and 
	False otherwise.'''
	i = 0
	while i < len(lst) - 1:
		if lst[i] > lst[i+1]:
			return False
		i += 1
	return True

def is_anagram(str1, str2):
	'''Takes two strings and returns True if they are 
	anagrams.'''
	if len(str1) != len(str2):
		return False
	for i in str1:
		if i not in str2:
			return False
	return True

