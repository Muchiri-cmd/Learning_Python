class User():
	#a profile for a user
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.login_attempts=0
		
	def describe_user(self):
		print(self.name.title()+self.age)
		
	def greet_user(self):
		#prints special message to user
		print(" Hi, "+self.name.title()+ " hope your doing fine !")
	def increment_login_attempts(self):
		#shows number of login attempts
		self.login_attempts+=1
		print("login attempts are now: "+str(self.login_attempts))
		
	def reset_login_attempts(self):
		#resets login attemts to 0
		self.login_attempts=0
		print("successful reset,attempts are now "
		 +str(self.login_attempts))
