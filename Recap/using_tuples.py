# Parentheses are optional, but always recommended.
# Explicit is better than implicit.

zoo = ('ostrich', 'tortoise', 'lion', 'cheetah')
print 'Number of animals in the zoo is', len(zoo)
new_zoo = 'baboon', 'python', 'black mamba', 'hyena', 'monkey', zoo
print 'Number of cages in the new zoo is', len(new_zoo)
print 'All animals in the new zoo are', new_zoo
print 'Animals brought from the old zoo are', new_zoo[5]
print 'Last animal brought from the old zoo is', new_zoo[5][3]
print 'Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[5])