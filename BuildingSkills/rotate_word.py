def rotate_word(word, n):
	'''Returns a new string that contains the 
	letters from the original string rotated by 
	the given figure.
	ord(): inbuilt function, converts a character 
	to numeric code.
	chr(): inbuilt function, converts numeric 
	code to characters.'''
	x = ''
	for i in word:
		num = ord(i)+n
		if num > 122:
			num -= 26
		if num < 97:
			num += 26
		x += chr(num)
	return x
	
print rotate_word('melon', -10)