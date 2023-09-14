import re
x='From : Using the : ccharacter'
y=re.findall('^F.+?',x)
print(y)
#prints shortest match ('From:')