class Restaurant():
	#A simple model for a restaurant
	
	def __init__(self,name,cuisine):
		#initialize restaurant name and cuisine type
		self.name=name
		self.cuisine=cuisine
		
	def describe_restaurant(self):
		#print restaurant information
		print(self.name.title()+self.cuisine.title)
		
	def open_restaurant(self):
		print(self.name.title()+" is now open!")
		
		
class Restaurant():
 Ibis=Restaurant('Ibis','B')
 print("my restaurant's name is "+Ibis.name.title()+ ".")
 print("my restaurant is "+Ibis.cuisine+".")
 
 Ibis.open_restaurant()
	
