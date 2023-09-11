from random import randint

class Die():
	"""represents a dice that can be rolled"""
	def __init__(self,sides=20):
		self.sides=sides
		
	def roll_dice(self):
		"""returns a number between 1 and number of sides"""
		return randint(1,self.sides)
		
#make a 20 sided die and roll it 10 times
d20=Die()
results=[]
for roll_num in range(10):
	result=d20.roll_dice()
	results.append(result)
	
	
	
print("\n10 rolls of a 20-sided die:")
print(results)
		
