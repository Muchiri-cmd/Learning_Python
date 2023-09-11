"""a Program that asks user why the love programming and stores the 
answers in a text file"""
filename='programmingpoll.txt'

print("press q to quit poll")
while True:
	response=input("why do you love programming ?")
	
	if response =='q':
		print("Thanks for taking the poll")
		break;
	else:
		with open(filename,'a')as f:
			f.write(response+"\n")
			
			
with open(filename)as f:
	lines=f.readlines()

for line in lines:
	print(line.rstrip())
	

			
			
	

