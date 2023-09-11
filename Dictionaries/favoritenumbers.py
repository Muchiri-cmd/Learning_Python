favorite_numbers={
	'Alex':[15,17],
	'Edwin':[21,33],
	'Lui':[58,68],
	'Davinci':[48,1],
	'Foden':[47,12],
	}

for name,numbers in favorite_numbers.items():
	print(name +" favorite numbers are:")
	for favorite_number in numbers:
		print(favorite_number)

