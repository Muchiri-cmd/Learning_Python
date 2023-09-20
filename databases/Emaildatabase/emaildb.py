import sqlite3
# a python program that creates a db,checks if an email entry is in a database INSERT if not and UPDATE if it exists
#open
conn=sqlite3.connect('emaildb.sqlite')#connection (access) to db,creates if non exists
cur=conn.cursor()#handle.send n recv sql cmds

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT,count INTEGER)''')

fname=input("Enter file name: ")
if (len(fname)<1): fname='email_list.txt'
fhandle=open(fname)

for line in fhandle:
    if not line.startswith('From: '):continue
    pieces=line.split()
    email=pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email= ?  ',(email,)) 
    '''qn mark acts as placeholder  to prevent SQL Injection,
    replaced w var email'''

    row=cur.fetchone()#first 1
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count)VALUES (?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE email  ?',(email,))
    conn.commit() #writes to disk(for bulk done in intervals)-takes time

#https://www.sqlite.org/lang_select.html
sqlstr='SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'#top 10

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])#email,count

cur.close()

