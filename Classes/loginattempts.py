class User():
	#a profile for a user
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.login_attempts=0
		
	def describe_user(self):
		#prints user info
		print(self.name.title()+self.age)
		
	def greet_user(self):
		#prints special message to user
		print(" Hi, "+self.name.title()+ "Welcome!")
	def increment_login_attempts(self):
		#shows number of login attempts
		self.login_attempts+=1
		print("login attempts are now: "+str(self.login_attempts))
	def reset_login_attempts(self):
		#resets login attemts to 0"""
		self.login_attempts=0
		print("successful reset,attempts are now "
		 +str(self.login_attempts))
	
user_1=User('davis',17)
user_2=User('lance',18)
user_3=User('luiz',16)
print("user1's name is,"+user_1.name.title())
print("user1s age is,"+str(user_1.age))
user_1.greet_user()
user_2.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
 
