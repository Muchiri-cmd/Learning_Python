"""program that prompts for 2 numbers,adds them and prints a result"""
print("press q to quit program")
while True:
	number1=input("enter first number:\n")
	if number1=='q':
		break;
	number2=input("enter second number:\n")
	if number2=='q':
		break;
	else:
	
		try:
			result=int(number1)+int(number2)
			print("The result is:"+str(result))
			
		except ValueError:
			print("\ntry entering integer values only")



