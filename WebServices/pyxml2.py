import xml.etree.ElementTree as ET
input='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Davis</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Abigael</name>
        </user>
    </users>
</stuff>
'''

stuff=ET.fromstring(input)
print(stuff)
lst=stuff.findall('users/user')
print('user count:',len(lst))
for item in lst:
    print('Name',item.find('name').text)
    print('id',item.find('id').text)
    print('Attribute',item.get("x"))