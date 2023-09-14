'''
file = open(mbox-short.txt)
for line in file:
    line.rstrip()
    if line.startswith('From:'):
        print (line)
'''

import re
file=open('mbox-short.txt')
for line in file:
    line.rstrip()
    if re.search('^From:',line):
        print(line)
