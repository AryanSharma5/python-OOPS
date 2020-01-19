class Employee:
	
	def __init__(self, ename, esalary, deptno):
		self.name = ename
		self.salary = esalary
		self.department = deptno

	def showEmployee(self):
		print(f'Employee Name : {self.name}\nEmployee Salary : {self.salary}\n Employee Department :{self.department}\n')

class Salesman(Employee):

	def __init__(self, ename, esalary, deptno, comm):
		self.Commission = comm
		super().__init__(ename, esalary, deptno)

	def showEmployee(self):
		super().showEmployee()
		print(f'Employee Name : {self.name}\nEmployee Salary : {self.salary}\n Employee Department :{self.department}\n Commission : {self.Commission}')


obj1 = Salesman('Aryan', '56000', '101', 25000)
obj1.showEmployee()
#print(f'Commission : {obj1.Commission}')