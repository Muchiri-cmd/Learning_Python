from random import randint

class Die():
	def __init__(self,default_value=6):
		self.default_value=default_value
	
	def roll_dice(self):
		"""Return a statement between 1 and the number of sides"""
		return randint(1,self.default_value)
		
#make a 10-sided die and show the results of 10 rolls
d10=Die()

results=[]
for roll_num in range(10):
	result=d10.roll_dice()
	results.append(result)
	
print("\n10 rolls of a 10-sided die:")
print(results)
	
	
#make a 6-sided die and show the results
d6=Die()
results=[]
for roll_num in range(6):
	result=d6.roll_dice()
	results.append(result)
		
print("\n6 rolls of a 6-sided die:")
print(results)


#make a 20-sided die
d20=Die()
results=[]

for roll_num in range(20):
	result=d20.roll_dice()
	results.append(result)
		
print("\n20 rolls of a 6-sided die:")
print(results)










