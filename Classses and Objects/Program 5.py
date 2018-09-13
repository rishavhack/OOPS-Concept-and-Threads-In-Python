class Student():
	def __init__(self,n='',m=0):
		self.name = n
		self.marks = m
        
	def display(self):
		print "Hi ",self.name
		print "Your marks ",self.marks
        
	def calculate(self):
		if(self.marks >= 600):
			print "You got first grade"
		elif(self.marks >= 400):
			print "You got second grade"
		else:
			print "Failed"

n = int(input("How many Student ?"))
i = 0
while (i<n):
	name = raw_input("Enter Student Name: ")
	marks = int(input("Enter MAeks :"))
	s = Student(name,marks)
	s.display()
	s.calculate()
	i += 1
