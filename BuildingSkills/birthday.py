import random

def has_duplicates(lst):
	'''Takes a list and returns True if any element 
	appears more than once. Does not modify the 
	original list.'''
	t = lst[:]
	t.sort()
	for i in range(len(t)-1):
		if t[i] == t[i+1]:
			return True
	return False

def birthdays(n):
	'''Returns a random list of (n) integers between
	1 and 365.''' 
	x = list()
	for i in range(n):
		y = random.randint(1, 365)
		x.append(y)
	return x

def shared_bdays(students, samples):
	'''Generate (samples) sample of (students) 
	students and count how many have at least a 
	pair of students with the same birthday.'''
	count = 0
	for i in range(samples):
		x = birthdays(students)
		if has_duplicates(x):
			count += 1
	return count


print shared_bdays(23, 1000)