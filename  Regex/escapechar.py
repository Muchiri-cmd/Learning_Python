import re
x='You just received $10.00 from Fiverr.'
y=re.findall('\$[0-9.]+',x)
print(y)#['10.00']