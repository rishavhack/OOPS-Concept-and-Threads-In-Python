class sample:
	x = 10
	@classmethod
	def modify(cls):
		cls.x = cls.x + 1

s1 = sample()
s2 = sample()
print 'x in s1 = ', s1.x
print 'x in s2 = ', s2.x
s1.modify()
print 'x in s1 = ',s1.x
print 'x in s2 = ',s2.x
