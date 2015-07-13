import urllib
import lxml.html


test_url = 'http://www.kcgcollege.ac.in/'
conn = urllib.urlopen(test_url)

dom =  lxml.html.fromstring(conn.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
   print link

conn.close()
