shoplist = ['mango', 'apple', 'banana', 'jackfruit', 'orange', 'carrot']
name = 'Aisha'

# Indexing (Subscription operation)
i = 0
while i < len(shoplist):
	print 'Item {} is {}'.format(i, shoplist[i])
	i += 1
print '\nCharacter 0 is', name[0]

# Slicing on a list
print '\nItem 1 to 3 is', shoplist[1:3]
print 'Item 2 to the end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item -2 to end is', shoplist[-2:]
print 'Item start to end is', shoplist[:]

#Slicing on a string
print '\nCharacters 1 to 3 is', name[1:3]
print 'Characters 2 to end is', name[2:]
print 'Characters 1 to -1 is', name[1:-1]
print 'Characters -2 to end is', name[-2:]
print 'Characters start to end is', name[:]

# Steps for Slicing
print '\nshoplist[::1] is', shoplist[::1]
print 'shoplist[::2] is', shoplist[::2]
print 'shoplist[::-1]', shoplist[::-1]
print '\nCharacters[::2]', name[::2]
print 'Characters[::-1]', name[::-1]