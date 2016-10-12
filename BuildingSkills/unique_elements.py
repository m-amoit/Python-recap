def remove_duplicates(lst):
	'''Returns a new list with only the unique 
	elements from the original.'''
	new_list = []
	for i in lst:
		if i not in new_list:
			new_list.append(i)
	return new_list


