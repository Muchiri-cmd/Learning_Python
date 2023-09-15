import urllib.request,urllib.error,urllib.parse
import json

serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address=input("Enter location:")
    if len(address) <1:break
    url=serviceurl+urllib.parse.urlencode({'address':address})

    print('retrieving...',url)
    data=urllib.request.urlopen(url)
    info=data.read().decode()
    print ('retrieved',len(info),'characters')

    try:
        js=json.loads(info)
    except:
        js=None

    print(js)
    if not js or 'status' not in js or js['status']!='OK':
        print('Failure to retrieve===')
        print(info)
        

    latitude=js["results"][0]["geometry"]["location"]["lat"]
    longitude=js["results"][0]["geometry"]["location"]["lng"]
    print('latitude:',latitude,'longitude:',longitude)
    location=js['results'][0]['formatted_address']
    print(location)