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

obj1 = new_calcultor("whatname")
results = obj1.add(3,4)
results_2 = obj1.sub(5,2)
print(results)
print(results_2)




