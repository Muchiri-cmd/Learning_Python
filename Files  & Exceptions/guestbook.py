filename='guest_book.txt'

while True:
	"""a loop that asks user for name input"""
	print("press q to quit")

	name=input("Enter your name ")
	if name !='q':
		name=name
	else:
		print("Thanks for the taking the poll")
		break;
		
	with open(filename,'a')as f:
		f.write(name+"\n")
	

		
