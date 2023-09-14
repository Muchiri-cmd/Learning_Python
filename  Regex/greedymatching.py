import re
x='From:Using the : character '
y=re.findall('^F.+:',x)
print(y)
#prints From:Using the :
#repeat chars (* and +) push outward to match largest possible string