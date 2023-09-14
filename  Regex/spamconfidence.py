import re
file=open('mbox-short.txt')
numlist=list()
for line in numlist:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1 : continue
    num=float(stuff[0])
    numlist.append(num)
print('maximum:',max(numlist))