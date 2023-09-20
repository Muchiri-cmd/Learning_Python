import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('tracksdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
                  
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
     len INTEGER , rating INTEGER , count INTEGER             
);
''')

fname=input("Enter file name: ")
if len(fname)<1:fname='Library.xml'

def lookup(elem,key):
    found=False
    for child in elem:
        if found:
            return child. text#returns value of the found key
        if child.tag=='key' and child.text==key:
            found=True
    return None

stuff=ET.parse(fname)
all=stuff.findall('dict/dict/dict')#3rd level of dicts(tracks)
print("Dict count",len(all))

for entry in all:
    if (lookup(entry,'Track ID')is None):continue
    name=lookup(entry,'Name')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    count=lookup(entry,'Play Count')
    rating=lookup(entry,'Rating')
    length=lookup(entry,'Total Time')

    if name is None or artist is None or album is None:
        continue
    print(name,artist,album,count,rating,length)

    cur.execute('''INSERT OR IGNORE INTO Artist(name)VALUES(?)''',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id=cur.fetchone()[0]#foreign key for album

    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id)VALUES(?,?)''',(album,artist_id))
    cur.execute('SELECT  id FROM Album WHERE title=?',(album,))
    album_id=cur.fetchone()[0]#foreign key for track

    cur.execute('''INSERT OR REPLACE INTO Track
                (title,album_id,len,rating,count)VALUES(?,?,?,?,?)''',
                (name,album_id,length,rating,count))
    
    conn.commit()