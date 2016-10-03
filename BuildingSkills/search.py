def find(word, letter):
	'''Takes a character and finds the index where
	that character appears'''
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1