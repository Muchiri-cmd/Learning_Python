class Car():
	#A simple car model
	def __init__(self,brand,model):
		self.brand=brand
		self.model=model
		
	def describe_car(self):
		#Print car info
		print(self.brand.title()+self.brand.model.title())
		
	def availability(self):
		#show if car is in stock 
		print(self.car.brand.title()+" is available !")
		
class Car():
  in_cart=Car('mercedes','rx37')
  print("the car i ordered is, "+in_cart.brand.title())
  print("the model is, "+in_cart.model.title())
  
  
  in_bin=Car('nissan','skyline')
  print("the car i consider second is, "+in_bin.brand.title())
  print("the model is ,"+in_bin.model.title())
  
  in_trash=Car('mazda','demio')
  print("i dont want a "+in_trash.brand.title())
  
		
