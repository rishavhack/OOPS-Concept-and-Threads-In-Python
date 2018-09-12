class Sample(object):
	#This is Constructor
	def __init__(self):
		self.x = 10
	 #This is an instance method
	 def modify(self):
	 	self.c += 1
s1 = Sample()
s2 = Sample()
print 'x in s1',s1.x;
print 'x in s2',s2.x;
s1.modify()
	print 'x in s1',s1.x;
print 'x in s2',s2.x;

		