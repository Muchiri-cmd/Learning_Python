filename='learningpython.txt'

with open(filename)as f:
	#reading file content in a list
	lines=f.readlines()
for line in lines:
	print(line.rstrip())

with open(filename)as f:
	#reading entire file
	contents=f.read()
print(contents)

with open(filename)as f:
	#reading file content line by line
	for line in f:
		line=line.replace('python','c')
		print(line.rstrip())
		
		
