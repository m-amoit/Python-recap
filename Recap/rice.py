class rice(object):
	"""Various rice dishes."""
	def __init__(self, water, salt):
		self.water = water
		self.salt = salt

	def plainwhite(self):
		print 'Plain boiled white rice. Salted.'

	def vegrice(self, *args):
		self.args = args
		print '\nRice cooked in these vegetables:', 
		for arg in self.args: print arg,

	def pilau(self, beef, *args):
		self.beef = beef
		self.args = args
		print '\n\nMain ingredient is', self.beef, ' It may include', 
		for i in self.args: print i,

	def jolofrice(self):
		print '\n\nI really have no idea about this one. I only see it in West African tv shows.'


y = rice('water', 'salt')
y.plainwhite()
y.vegrice('carrot', 'peas', 'greenpepper')
y.pilau('fried beef', 'garlic', 'soysauce', 'cumin')
y.jolofrice()