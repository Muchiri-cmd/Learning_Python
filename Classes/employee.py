#a program for employee and employee methods
class Employee():
	"""an employee class"""
	
	def __init__(self,lastname,firstname,salary):
		self.lastname=lastname.title()
		self.firstname=firstname.title()
		self.salary=salary
		fullname=firstname+lastname
		
	def give_default_raise(self,bonus=5000):
		self.salary+=bonus
		
	def show_annual_salary(self,fullname,salary):
		"""prints annual salary inclusive of bonus"""
		print(fullname+"earns a total of: "+salary)
	
	def show_bonus(self,fullname,bonus):
		"""prints bonus earned"""
		print(fullname+"has a bonus of: "+bonus)
		




		
			
			

	
