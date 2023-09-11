def build_profile(first, last, **user_info):
	#Build a dictionary containing everything known about a user.
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Dave', 'Kennedy',
                              location='States',
							  field='penetration testing')
print(user_profile)

