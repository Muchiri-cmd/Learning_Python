import json

data='''{
    "name":"Davis",
    "phone" : {
        "type:":"intl",
        "number":"+254 113708866"
    },
    "email":{
        "hide":"yes"
    }
}'''

info=json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])