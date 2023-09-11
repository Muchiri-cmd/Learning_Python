"""program that reads contents off files and prints them to screen"""
def openfile(filename):
	try:
		with open(filename)as f:
			content=f.read()
			print(content)
	except FileNotFoundError:
			pass

openfile('cats.txt')
openfile('dogs.txt')
