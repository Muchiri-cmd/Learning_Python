responses={}

polling_active=True
while polling_active:
	name=input("Whats your name friend?")
	response=input("If you could travel one place in the world,where would it be?")
	
	responses[name]=response
	repeat=input("You could also have someone else take this poll by pressing n.Are you done?(y/n)")	
	if repeat=='y':
		polling_active=False
print("\n----poll results---")
for name,response in responses.items():
	print(name+" would like to visit "+response+".")
