class Student():
	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setMarks(self,marks):
		self.marks = marks

	def getMarks(self):
		return self.marks

n = int(input("How many student?"))
i=0

while i<n:
	s = Student()
	name = raw_input("Enter name: ")
	s.setName(name)
	marks = raw_input("Enter Marks")
	s.setMarks(marks)
	#Reterive data from student class instance
	print "Hi ",s.getName()
	print "Marks " ,s.getMarks()
	i += 1