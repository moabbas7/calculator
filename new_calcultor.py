class new_calcultor():

	def __init__(self,name):
		self.name = name

	def add(self,a,b):
		result =a+b
		return result

	def sub(self,a,b):
		return (a-b)

	def mul(self,a,b):
		return (a*b)

	def div(self,a,b):
		return (a/b)

class ScientificCalculator(new_calcultor):

	def power(self,a):
		return a*a

def prints_something(some_string):
	print("inside a function ouside a class"+some_string)


