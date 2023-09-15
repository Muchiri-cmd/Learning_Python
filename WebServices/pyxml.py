import xml.etree.ElementTree as ET
data='''<person>
    <name>Davis</name>
    <phone type="intl">
        +254 113708866
    </phone>
    <email hide="yes"/>
</person>'''

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))