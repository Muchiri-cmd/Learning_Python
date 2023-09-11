"""program that accepts 2 parameters city,country names and return a 
single string in the form City,Country"""

def city_country(city,country,population=0):
	"""generate a formatted city country name"""
	if population:
		modified_name=city+","+country+" population-"+str(population)
		return modified_name.title()
	else:
		modified_name=city+","+country
		return modified_name.title()
	
	
	
