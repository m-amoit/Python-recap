
fin = open('words.txt')

def read_text():
	'''Reads words.txt and prints words with more
	than 20 characters'''
	for line in fin:
		word = line.strip()
		if len(word) > 20:
	 		print word

def has_no_e(word):
	'''Returns True if the given word has no 
	letter 'e' in it'''
	if 'e' not in word:
		return True

def find_text():
	'''Reads words.txt and prints words without
	letter e in them.'''
	for line in fin:
		if has_no_e(line) is True:
			print line

def avoids(word, forbidden):
	'''Takes a word and a string of forbidden 
	letters and returns True if the word doesn't 
	use any of the forbidden letters'''
	for i in word:
		if i in forbidden:
			return False
	return True

def count_words():
	'''Prompts the user for a string of forbidden
	letters and returns the number of words that
	don't contain any of them.'''
	count = 0
	x = raw_input('Enter string of forbidden letters: ')
	for line in fin:
		if avoids(line, x) is True:
			count += 1
	return count

def uses_only(word, available):
	'''Takes a word and a string of letters and 
	returns True if the word contains only 
	letters in the list'''
	for i in word:
		if i not in available:
			return False
	return True

def uses_all(word, required):
	'''Takes a word and a string of letters and 
	returns True if the word uses all the required
	letters at least once.'''
	return uses_only(required, word)

def is_abecedarian(word):
	'''Returns True if the letters in a word appear
	in alphabetical order (double letters are ok)
	ord(): converts a character to numeric code.
	'''
	word = word.lower()
	digit = None
	for i in word:
		if ord(i) < digit:
			return False
		digit = ord(i)
	return True


if __name__ == '__main__':
	print is_abecedarian('aeiou')
