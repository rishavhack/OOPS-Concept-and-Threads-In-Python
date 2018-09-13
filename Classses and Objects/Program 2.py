class Student():
	def __init__(self,n='',m=0):
		self.name = n
		self.marks = m

	def talk(self):
		print "Hi I am ",self.name
		print "My marks is ",self.marks

print 'Constructor is called without any arguments'
s1  = Student()
s1.talk()

print 'Constructor is called any arguments'
s1  = Student('Maa',50)
s1.talk()	