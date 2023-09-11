class Restaurant():
	#A simple model for a restaurant
	
	def __init__(self,name,cuisine):
		"""initialize restaurant name and cuisine type"""
		self.name=name
		self.cuisine=cuisine
		self.served=0
		
		
	def describe_restaurant(self):
		#print restaurant information
		description=(self.name.title()+self.cuisine.title())
		return description
		
	def open_restaurant(self):
		print(self.name.title()+" is now open!")
		
	def number_served(self):
		#prints no of customers served
		print("This restaurant has served,"+str(self.served)+" customers")
	
	def update_served(self,served):
		"""prints number of customers served by method"""
		self.served=served
		
	def increment_served(self,served):
		self.served+=served
		return self.served
			
Ibis=Restaurant('Ibis','French Cuisine')
print("my restaurant's name is "+Ibis.name.title()+ ".")
print("my restaurant is "+Ibis.cuisine+".")
 
Ibis.describe_restaurant()
Ibis.open_restaurant()
Ibis.number_served()
 
Ibis.served=23
Ibis.number_served()
 
Ibis.update_served(23500)
Ibis.number_served()
Ibis.increment_served(100)
Ibis.number_served()
 
class IceCreamStand(Restaurant):
	#A branch of the restaurant that deals with Icecream
	def __init__(self,name,cuisine):
	    #initialize attributes of parent class
		super().__init__(name,cuisine)
		self.flavors=['vanilla','chocolate','strawberry']
	
	 
	def show_flavors(self):
		"""prints flavors available"""
		print("The restaurant serves:")
		for flavor in self.flavors:
			print(flavor)
	 
	 
your_order = IceCreamStand('Ibis','Ice cream' )
your_order.show_flavors()




	 

	    



		

 
 
	
