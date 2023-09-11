cities={
	'Nairobi':['kenya','49million','mostcorrupt'],
	'Rio':['Brazil','72million','talented athletes'],
	'Berlin':['Germany','59million','developed'],
	}
	
for city,information in cities.items():
	print("\n"+city.title())
	for info in information:
		print("\t" +info)
