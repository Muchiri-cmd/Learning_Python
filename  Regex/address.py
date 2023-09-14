import re

x='From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('^From (\S+@\S+)',x)
print(y) #Stephen.marquard@uct.ac.za

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)#[csev@umich.edu,cwen@iupui.edu]