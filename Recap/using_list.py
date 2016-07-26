shoplist = ['mango', 'orange', 'apple', 'broccoli']

print 'I have', len(shoplist), 'items to purchase'

print 'These items are:', 
for item in shoplist: print item,

print '\nI also have to buy dhania'
shoplist.append('dhania')
print 'My shopping list now is', shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list now is', shoplist
print 'The first item I will buy is', shoplist[0]
print 'I bought the', shoplist[0]
del shoplist[0]
print 'My shooping list now is', shoplist
