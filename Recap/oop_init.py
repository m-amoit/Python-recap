class Person(object):
	"""Introducing the __init__ method
	
	Do not explicitly call the init method but pass the arguments
	in the parenthesis following the class name when creating a new instance of the class."""
	def __init__(self, name):
		self.name = name
	def say_hi(self):
		print 'Hello, my name is', self.name

Person('Aisha').say_hi()
		