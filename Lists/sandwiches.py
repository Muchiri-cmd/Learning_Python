sandwich_orders=['tuna sandwiches','bbq sandwich','ham sandwich','omlette sandwich']
finished_sandwiches=[]
for sandwich_order in sandwich_orders:
	print("i made your "+sandwich_order+".")
	
while sandwich_orders:
	finished_sandwiches=sandwich_orders.pop()
	print(finished_sandwiches+" was made")
	
	
