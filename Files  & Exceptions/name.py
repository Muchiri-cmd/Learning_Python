#program that asks user for data and writes in a file
name=input("enter name")

filename='name.txt'
with open(filename,'w')as file_object:
	file_object.write("\n"+name)
	print("\n"+name)


