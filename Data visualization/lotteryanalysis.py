from random import choice

possibilities=[1,2,3,4,5,6,7,8,9,10,'a','b','c']
def get_winning_ticket(possibilities):
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
    return winning_ticket

def check_ticket(played_ticket,winning_ticket):
    """check all elements in the played ticket,if they are not in the 
    winning ticket return false"""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    #we must have a winning ticket
    return True

def make_random_ticket(possibilities):
    """return a random ticket from a set of possibilities"""
    ticket=[]
    while len(ticket)<4:
        pulled_item=choice(possibilities)
        """only add the pulled item to the ticket if it hasnt already 
        been pulled"""
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket
possibilities=[1,2,3,4,5,6,7,8,9,10,'a','b','c']
winning_ticket=get_winning_ticket(possibilities)
plays=0
won=False

#lets see a max number of tries in case this takes forever
max_tries=1_000_000

while not won:
    new_ticket=make_random_ticket(possibilities)
    won=check_ticket(new_ticket,winning_ticket)
    plays+=1
    if plays >=max_tries:
        break

if won:
    print("we have a winning ticket")
    print(f"your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"it only took {plays} tries to win!")

else:
    print(f"Tried {plays} times,without pulling a winnner. :(")
    print(f"your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")