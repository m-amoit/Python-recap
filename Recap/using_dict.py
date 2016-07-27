# address book
ab = {'Mick' : 'mick@mouse.com',
	  'Larry' : 'larry@wall.org',
	  'Miriam' : 'miriam@worldvision.org',
	  'Sarah' : 'sarah@winrock.org',
	  'Ronald' : 'roouma@hotmail.com',
	  'Amoit' : 'amoiteumot@gmail.com',
	  'Spammer' : 'spam@unknown.ac.ke',}

print "Mick's address is", ab['Mick']
# Deleting a key value pair
del ab['Spammer']

print '\nThere are {} contacts in the address book\n'.format(len(ab))

for name, address in ab.items():
	print 'Contact {} at {}'.format(name, address)

# Adding a key value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print "\nGuido's address is", ab['Guido']
