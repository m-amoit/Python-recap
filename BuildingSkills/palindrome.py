
def is_palindrome(word):
	'''Takes a string argument and returns True if
	it is a palindrome and False otherwise
	'''
	if word == word[::-1]:
		return True
	return False

print is_palindrome('redivider')


