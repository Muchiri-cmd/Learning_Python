def car_profile(name,model,**extras):
		profile={}
		profile['manufacturer_name']=name
		profile['model_name']=model
		
		for key,value in extras.items():
			profile[key]=value
		return profile
		
		
info=car_profile('Enzo','ferrari',
				  color='red',
				  speed='360 mph',
				  make='viper')
				  
print(info)
				  


