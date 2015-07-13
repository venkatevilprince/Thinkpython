import urllib2

import lxml.html

#for line in data:
#    line = line.strip()
#    if 'href' in line and 'shtml' in line:
#       print line
test_url = 'http://www.kcgcollege.ac.in/'

def get_links_from_url(web_url):
    conn = urllib2.urlopen('http://www.kcgcollege.ac.in/')
    data=conn.read().split("</a>")
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
                    linklist.append(link)
    return linklist

#dom =  lxml.html.fromstring(conn.read())

#for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
#   print link

test_links = get_links_from_url(test_url)

for l in test_links:
    print l
