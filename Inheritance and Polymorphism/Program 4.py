class Father:
	def __init__(self):
		self.property = 800000

	def display(self):
		print "Property = ",self.property

class Son(Father):
	def __init__(self):
		self.property = 1000000

	def display(self):
		print 'Child =',self.property

s = Son()
s.display()