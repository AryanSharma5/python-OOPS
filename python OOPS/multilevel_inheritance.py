class Father:
	def FatherProperty(self):
		print('Father property used for home')

class Mother(Father):
	def MotherProperty(self):
		print('Mother property used for farming')

class child(Mother):
	def childProperty(self):
		print('child property used for playground')

	def FatherProperty(self):
		print('Father property now used by child for cricket ground.')


obj1 = child()
obj1.FatherProperty()
obj1.MotherProperty()
obj1.childProperty()
