class Father:
	def FatherProperty(self):
		print('Father Property')

class Mother:
	def MotherProperty(self):
		print('Mother Property')

class Child(Father,Mother):
	def ChildProperty(self):
		print('Child will inherit using Super : ')
		super().FatherProperty()
		super().MotherProperty()

obj1 = Child()
obj1.ChildProperty()
print('Calling Mother And Father by instance of the child Class:')
obj1.MotherProperty()
obj1.FatherProperty()