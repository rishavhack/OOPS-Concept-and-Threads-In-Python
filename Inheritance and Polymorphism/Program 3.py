class Father:
	def __init__(self):
		self.property = 80000

	def display(self):
		print "Father\'s property =",self.property


class Son(Father):
	pass #We do't want to write anything in the class

s = Son()
s.display()