class Emp:
	def __init__(self,id,name,salary):
		self.id = id
		self.name = name
		self.salary = salary

	def display(self):
		print "Id = ",self.id
		print "Name = ",self.name
		print "Salary = ",self.salary

class Myclass:
	# method to receive Emp class instance
	# and display employee details
	@staticmethod
	def mymethod(e):
		e.salary += 1000;
		e.display()

e = Emp(10,'Rishav',1500.75)
Myclass.mymethod(e)