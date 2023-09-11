import json

number=input("whats your favorite number?")

with open('favorite_number.json','w')as f:
	json.dump(number,f)
	print("Thanks ! i'll remember that.")
	
