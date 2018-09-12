class Student(object):
	"""docstring for Student"""
	def __init__(self):
		self.name = 'Rishav'
		self.age = 25
		self.marks = 88

	def talk(self):
		print "Hi I am ",self.name
		print "My age is ",self.age
		print "My marks is ",self.marks

##instance = Classname()
s1  = Student()
s1.talk()		