import urllib2
import csv
import threading
import Queue
import time
import requests
queue = Queue.Queue()
#for line in data:
#    line = line.strip()
#    if 'href' in line and 'shtml' in line:
#       print line
test_url = "http://www.kcgcollege.ac.in"

def get_links_from_url(web_url):
    #print web_url
    start = time.time()
    conn = requests.get(web_url)
    data = conn
    end = time.time()
    print end - start
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
                    
    queue.put([linklist])

start = time.time()
get_links_from_url(test_url)
test_links = queue.get()
end = time.time()
print end - start
with open('links.csv', 'w') as links:
    spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for l in test_links:
        spamwriter.writerow(l)

#start = time.time()        
#print test_links[0][1]
#first_sublink = get_links_from_url("http://www.kcgcollege.ac.in/index.shtml")
#end = time.time()
#print end - start
#for x in first_sublink:
#    for y in x:
#        print y
url1 = "http://www.kcgcollege.ac.in"
url2 = "http://www.stackoverflow.com"
url3 = "http://www.codeproject.com"

urls = [url1, url2, url3]
threads = []
response_list = []
for url in urls:
    print url
    t = threading.Thread(target=get_links_from_url, args=(url,))
    threads.append(t)
    t.start()
    

for thread in threads:
    thread_response = queue.get()
    response_list.append(thread_response)
    thread.join()


for t in response_list:
    #print t[0][0]
    for x in t:
        for y in x:
            print y
        print "\n\n\n\n\n\n"








