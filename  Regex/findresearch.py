'''
file = open ('mbox-short.txt')
for line in file :
    line=line.rstrip()
    if line.find('From:') >= 0:
        print(line)
'''
import re
file=open('mbox-short.txt')
for line in file:
    line.rstrip()
    if re.search('From:',line):
        print(line)