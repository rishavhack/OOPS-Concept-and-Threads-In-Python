class Myclass:
	# Method to calculate x to the power of n
	@staticmethod
	def mymethod(x,n):
		result = x**n
		print "{} to the power of {} is {}".format(x,n,result)

Myclass.mymethod(5,3)
Myclass.mymethod(5,4)