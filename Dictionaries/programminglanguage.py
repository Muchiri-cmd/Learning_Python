favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

pollers=['jen','edward','erin','cilian']
for name in favorite_languages.keys():
	print(name.title())

for name in pollers:
	if name in favorite_languages.keys():
		print(name.title()+ " ,thanks for responding ")
	elif name not in favorite_languages.keys():
		print(name.title()+" ,please take the poll")
