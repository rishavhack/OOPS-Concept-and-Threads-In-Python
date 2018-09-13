import math
class Sample:
	@staticmethod
	def calculate(x):
		result = math.sqrt(x)
		return result

num = float(input("Enter a number :"))

res = Sample.calculate(num)
print res
print '{:.2f}'.format(res)
