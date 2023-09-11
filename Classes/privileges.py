class User():
	#a profile for a user
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.login_attempts=0
		
	def describe_user(self):
		"""prints user info"""
		print(self.name.title()+self.age)
		
	def greet_user(self):
		"""prints special message to user"""
		print(" Hi, "+self.name.title()+ " hope your doing fine !")
	def increment_login_attempts(self):
		"""shows number of login attempts"""
		self.login_attempts+=1
		print("login attempts are now: "+str(self.login_attempts))
		
	def reset_login_attempts(self):
		#resets login attemts to 0
		self.login_attempts=0
		print("successful reset,attempts are now "
		 +str(self.login_attempts))
		 
class Admin(User):
	#a user that has privileges over user
	def __init__(self,name,age):
		#initializing attributes from parent class
		super().__init__(name,age)
		self.privileges=Privileges()
			
class Privileges():
	"""a simple class that shows admin privileges and is used as an 
	attribute  in parent class"""
	def __init__(self):
		#initialize the privileges attribute
		self.privileges=['can add post','can delete post','can ban user']
	
	def show_privileges(self):
		"""shows privileges"""
		print("admin can :")
		for privilege in self.privileges:
			print(privilege)
			
administrator=Admin('root',19)
administrator.privileges.show_privileges()
			
	


