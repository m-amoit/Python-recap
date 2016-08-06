class SchoolMember(object):
	"""Represents any school member"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print 'Initializing SchoolMember: {}'.format(self.name)

	def tell(self):
		"""Tell my details"""
		print 'Name: "{}" Age: "{}" '.format(self.name, self.age),

class ClassTeacher(SchoolMember):
	"""Represents a teacher"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print 'Initializing Teacher: {}'.format(self.name)

	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: {:d}'.format(self.salary)

class Student(SchoolMember):
	"""Represents a student"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print 'Initializing student: {}'.format(self.name)

	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: {:d}'.format(self.marks)

t = ClassTeacher('Mrs Kimei', 45, 76543)
s = Student('Aisha', 16, 750)

members = [t, s]
for member in members:
	member.tell()
		

		
		