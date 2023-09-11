current_users=['Take','Alex','Jack','Kim','Eliud']
new_users=['Take','Alex','Dani','Joe','ELIUD']

for current_user in current_users:
	current_user=current_user.lower()
	print("current users "+current_user)
for new_user in new_users:
	new_user=new_user.lower()
	print("new users "+new_user)
	
	
for new_user in new_users:
	if new_user in current_users:
		print('username has been taken')
	else:
		print('username available')
		

	
	







	




	

