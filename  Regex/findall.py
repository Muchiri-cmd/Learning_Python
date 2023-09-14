import re

x='My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x) #returns a list of numbers
print(y)
z=re.findall('[AEIOU]+',x)#returns empty list
print(z)