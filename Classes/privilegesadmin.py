from user import User 

class Admin(User):
	"""a user that has privileges over user """
	def __init__(self,name,age):
		"""initializing attributes from parent class"""
		super().__init__(name,age)
		self.privileges=Privileges()
			
class Privileges():
	"""a simple class that shows admin privileges and is used as an 
	attribute  in parent class"""
	def __init__(self):
		"""initialize the privileges attribute"""
		self.privileges=['can add post','can delete post','can ban user']
	
	def show_privileges(self):
		"""shows privileges"""
		print("admin can :")
		for privilege in self.privileges:
			print(privilege)
