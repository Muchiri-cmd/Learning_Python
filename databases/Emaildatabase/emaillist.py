import requests
url="http://mbox.dr-chuck.net/sakai.devel/4/5"
r=requests.get(url)

if r.status_code==200:
    email_list=r.text

    local_fname="/home/muchiri/Desktop/databases/email_list.txt"

    with open(local_fname,"w") as f:
        f.write(email_list)
        print("Successfully copied")
   
else:
    print("Failed to retrieve data.Status code : {r.status_code}")