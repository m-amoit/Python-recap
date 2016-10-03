def count(word, letter):
	'''Counts the number of times a letter appears
	in a string.'''
	count = 0
	for i in word:
		if i == letter:
			count += 1
	return count 

print count('banana', 'a')
