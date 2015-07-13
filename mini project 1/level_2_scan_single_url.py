import urllib
import csv
import time

import lxml.html

#for line in data:
#    line = line.strip()
#    if 'href' in line and 'shtml' in line:
#       print line
test_url = 'http://www.kcgcollege.ac.in/'

def get_links_from_url(web_url):
    print web_url
    start = time.time()
    conn = urllib.urlopen(web_url)
    end = time.time()
    print end - start
    data = ""
    for line in conn:
        line = line.strip()
        if 'a href' in line:
            data = data+line
    data = data.split("</a>")
    conn.close()
    linklist = []
    tag="<a href=\""
    endtag="\""
    for item in data:
        if "<a href" in item:
            try:
                ind = item.index(tag)
                item=item[ind+len(tag):]
                endt=item.index(endtag)
                link = item[:endt]
            except: pass
            else:
                pass
                if link[0] != '#':
                    if 'http' not in link:
                        link = web_url + link
                        linklist.append(link)
                    else:
                        linklist.append(link) 
                    
    return [linklist]

#dom =  lxml.html.fromstring(conn.read())

#for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
#   print link
start = time.time()
test_links = get_links_from_url(test_url)
end = time.time()
print end - start
with open('links.csv', 'w') as links:
    spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for l in test_links:
        spamwriter.writerow(l)
start = time.time()        
#print test_links[0][1]
first_sublink = get_links_from_url("http://www.kcgcollege.ac.in/index.shtml")
end = time.time()
print end - start
#for x in first_sublink:
#    for y in x:
#        print y
