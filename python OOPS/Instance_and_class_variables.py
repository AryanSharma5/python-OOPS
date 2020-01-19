#Instance Variable

#we can access class variables by self and by classname also. 
#By using class name we would change that class variable for all instances of that class. 
#But by using self we can change the class variable for each and every instance variable seperately.

class Employee:
	#class variables
	num_of_emp = 0
	raise_amt = 1.04

	def __init__(self,first,last,pay):
		
		#instance variables
		self.first = first
		self.last = last
		self.pay = pay

		#accessing class variable by classname
		Employee.num_of_emp += 1

	def print_email(self):
		return self.first + '.' + self.last + '@gmail.com'

	def set_raise(self):
		#accessing class variable by instance
		self.raise_amt = 2.04
		return self.raise_amt

print(f'number of employees before creating instances : {Employee.num_of_emp}')
emp1 = Employee('aryan','sharma',50000)
emp2 = Employee('xyz','sharma',20000)
print(f'number of employees after creating instances : {Employee.num_of_emp}')

print(f'raise in amount of emp1 (accessing using instance) : {emp1.set_raise()}')
print(f'raise in amount of emp2 : {Employee.raise_amt}')

#print(emp1.print_email())
#print(emp2.print_email())
print(Employee.print_email(emp2))