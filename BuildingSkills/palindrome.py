
'''A word is a palindrome if the first and last
letters are the same and the middle is a 
palindrome'''
def first(word):
	'''Returns the first letter of a given string
	'''
	return word[0]

def last(word):
	'''Returns the last letter of a given string
	'''
	return word[-1]

def middle(word):
	'''Returns the middle part of a given string,
	from the 2nd to the 2nd last letter'''
	return word[1:-1]

def is_palindrome(word):
	'''Takes a string argument and returns True if
	it is a palindrome and False otherwise
	'''
	if first(word) != last(word):
		return False
	if len(word) <= 2:
		return True
	else:
		word = middle(word)
		return is_palindrome(word)

print is_palindrome('redivider')


