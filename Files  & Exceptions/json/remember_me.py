import json
"""load the username if it has been stored previously otherwie,request user for input if 
username hasnt been stored previously"""

def get_stored_username():
    #retrieves stored usernames
    filename='username.json'
    try:
        with open(filename)as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    username=input("whats your name ?")
    filename='username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    #Greet the user by name.
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username =get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

