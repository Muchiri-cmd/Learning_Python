from random import randint
x=randint(1,6)

class Die():
    #Reps a die that can be rolled.
    def __init__(self,sides=6):
        #initialize the die.
        self.sides=sides
    def roll_die(self):
        #return a number between 1 and number of sides
        return randint(1,self.sides)
    
#Make a 6-sided die and show the results of 10 rolls
d6=Die()

results=[]
for roll_num in range(10):
    result=d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die")
print(results)

#do the same for other dies ,20-sided eg

