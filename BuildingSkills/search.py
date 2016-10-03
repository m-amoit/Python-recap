def find(word, letter, index):
	'''Takes a character and finds the index where
	that character appears.
	Starts the seach from the given index'''
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1

print find('supersilious', 's', 3)