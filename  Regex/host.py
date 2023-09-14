data='From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

'''atpos=data.find('@')
sppos=data.find(' ',atpos)
host=data[atpos+1:sppos]
print(host)#utc.ac.za
'''
#regex
import re
y=re.findall('^From .*@([^ ]*)',data)
print(y)#utc.ac.za