from bisect import *

def word_list():
	'''Reads the file words.txt and builds a list with
	one element per word.'''
	word_list = []
	x = open('wordplay/words.txt')
	for word in x:
		y = word.strip()
		word_list.append(y)
	return word_list

def bisect_list(word_list, word):
	'''Check whether a word is in a list using
	bisection search. 
	Assumes lst is sorted.'''
	i = bisect_left(word_list, word)
	if i != len(word_list) and word_list[i] == word:
		return True
	return False

def reverse(word_list, word):
	'''Checks if a word forms a reverse pair.'''
	x = word[::-1]
	return bisect_list(word_list, x)

def interlock(word_list, word):
	'''Check if a word can be split to form two interlocking words.
	Two words interlock if taking alternative letters
	from each forms a new word; e.g. 'shoe' and 
	'''
	word1 = word[::2]
	word2 = word[1::2]
	if bisect_list(word_list, word1) and bisect_list(word_list, word2):
		return True

def n_interlock(word_list, word, n):
	'''Check if a word can be split to form n 
	interlocking words.'''
	for i in range(n):
		new_word = word[i::n]
		if not bisect_list(word_list, new_word):
			return False
	return True

 