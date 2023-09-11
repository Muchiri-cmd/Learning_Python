filename='guest.txt'

#program that asks user for input 
name=input("enter your username\n")

with open(filename,'a')as f:
	f.write("\n"+name)

print("your name is now on my guest list thanks")
	



	
	


