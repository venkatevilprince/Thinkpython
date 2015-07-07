import urllib
s = raw_input("enter a zip code")
s=str(s)
conn = urllib.urlopen('http://www.uszip.com/zip/{}'.format(s))
for line in conn:
    line = line.strip()
    if 'Population' in line:
        print line
    if 'Longitude' in line: 
        print line
    if 'Latitude' in line: 
        print line

conn.close()
