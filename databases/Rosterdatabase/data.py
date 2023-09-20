import json

str_data=open('roster_data_sample.json').read()
json_data=json.loads(str_data)
print(json_data)