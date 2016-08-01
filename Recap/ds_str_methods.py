name = 'Aisha'
if name.startswith('Ai'):
	print 'Yes, the string starts with "Ai"'

if 'a' in name:
	print 'Yes, the string contains the character "a"'

if name.find('sha') != -1:
	print 'Yes, it contains the string "sha"'

delimiter = '_*_'
mylist = [2, 5, 7, 9]
print delimiter.join(str(i) for i in mylist)
print "".join(str(i) for i in mylist)
