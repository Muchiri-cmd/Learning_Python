import json

username=input("what is your name? ")
filename='username.json'

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("Will remember you when youre back, "+username+ "!")
    