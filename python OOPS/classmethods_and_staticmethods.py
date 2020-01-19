#classmethods :  
#class methods take cls as its first argument implicitly just like regular methods take self.
#we can use classmethods just like constructors.

#staticmethods :
#static methods are those methods which do not make use of any class variable or instance 
#variables in throughout their function.


class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	#class method
	@classmethod
	def fromstring(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)

	#static method
	@staticmethod
	def is_weekday(day):
		if day.weekday()==5 or day.weekday()==6:
			return True
		return False

emp_str_1 = 'aryan-sharma-50000'
emp_1 = Employee.fromstring(emp_str_1)
print(f'full name : {emp_1.first + emp_1.last}')

import datetime
mydate = datetime.date(2019,7,26)
print(f'weekday : {Employee.is_weekday(mydate)}')