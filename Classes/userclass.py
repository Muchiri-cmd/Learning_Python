class User():
	#a profile for a user
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def describe_user(self):
		print(self.name.title()+self.age)
		
	def greet_user(self):
		#prints special message to user
		print(" Hi, "+self.name.title()+ " hope your doing fine !")
		


user_1=User('davis',17)
user_2=User('lance',18)
user_3=User('luiz',16)
print("user1's name is,"+user_1.name.title())
print("user1s age is,"+str(user_1.age))
user_1.greet_user()
user_2.greet_user()
