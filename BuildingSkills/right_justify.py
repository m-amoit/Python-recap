def right_justify(x):
	'''
	a function that takes a string as a parameter and prints 
	the string with enough leading spaces so that the last letter of the 
	string is in column 70 of the display.
	'''
	column = 70 - len(x)
	y = ' '*column
	print y + x

right_justify('Bi Tatu') 
right_justify('Bi Tatu says she is a bitch')