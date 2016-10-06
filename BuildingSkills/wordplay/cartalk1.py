
def triple_double(word):
	'''Checks if a word contains three 
	consecutive doubles'''
	#Check for doubles
	i = 0
	count = 0
	while i < len(word) - 1:
		if word[i] == word[i+1]:
			count += 1
			i += 2
			if count == 3:
				return True
		else:
			count = 0
			i += 1
	return False

def find_triple_double():
	'''Finds a word with three consecutive doubles
	from the given list'''
	words = open('words.txt')
	for line in words:
		if triple_double(line):
			return line


print find_triple_double()