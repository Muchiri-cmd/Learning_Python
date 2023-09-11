def make_album(artist_name,album_title,tracks=''):
	description={'name':artist_name,'title':album_title}
	if tracks:
		description['tracks']=tracks
	return description
	
while True:
		print("(press q any time to quit)") 
		name=input("artist name ")
		if name =='q':
			break
		title=input("album title ")
		if title=='q':
			break
		tracks=input("tracks ")
	
		info=make_album(name,title,tracks)
		print(info)
	

	
	
	
	
