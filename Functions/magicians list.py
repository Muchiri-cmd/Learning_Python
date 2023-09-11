def show_magicians(unmodified_names,modified_names):

	while unmodified_names:
		current_names = unmodified_names.pop()
		modified_names.append(current_names)
	
def make_great(modified_names):

	for modified_name in modified_names:
		print("Great "+modified_name)
 
unmodified_names = ['Houdini', 'Dynamo', 'El matador']
modified_names = []

show_magicians(unmodified_names, modified_names)
make_great(modified_names)


