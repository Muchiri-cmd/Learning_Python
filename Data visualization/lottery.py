from random import choice

possibilities=[1,2,3,4,5,6,7,8,9,10,'a','b','c']
winning_ticket=[]
print("lets see what winning ticket is...")

"""we dont want to repeat winning numbers or letters so
we use a while loop"""

while len(winning_ticket)<4:
    pulled_item=choice(possibilities)
    """only add the pulled item to the winning ticket if 
    it hasnt already been pulled"""
    if pulled_item not in winning_ticket:
        print(f"we pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

