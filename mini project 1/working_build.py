import urllib2
import csv
import threading
import Queue
import time
import requests
import os

queue = Queue.Queue()
#for line in data:
#    line = line.strip()
#    if 'href' in line and 'shtml' in line:
#       print line
test_url = "http://www.kcgcollege.ac.in"
univ_dict = {}
reader_dict = {}

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
                    #print link
                    if link not in univ_dict.keys():
                        #print link
                        univ_dict[link] = link
                        if 'http' not in link:
                            link = web_url + '/' + link
                        linklist.append(link)
                    
    queue.put(linklist)
def create_reader_dict():
    readlinks = open("links.csv", 'r')
    reader = csv.reader(readlinks, delimiter=',', quotechar='|')
    for row in reader:
        for r in row:
            if r not in reader_dict.keys():
                reader_dict[r] = r
    readlinks.close()

def write_into_row_csv(url_list):
    with open('links.csv', 'a') as links:
        spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(url_list)

def write_into_row_csv_reduhandler(url_list):
    with open('links.csv', 'a') as links:
        spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        if os.stat("links.csv").st_size != 0:
            no_redundancy = []
            for url in url_list:
                if url not in reader_dict.keys():
                    no_redundancy.append(url)

            #no_redundancy.append(url)
            if(len(no_redundancy)>0):
                spamwriter.writerow(no_redundancy)
        else:
            #print "this happens"
            spamwriter.writerow(url_list)

create_reader_dict()
start = time.time()
get_links_from_url(test_url)
test_links = queue.get()
end = time.time()
print end - start
write_into_row_csv_reduhandler(test_links)
#start = time.time()        
#print test_links[0][1]
#first_sublink = get_links_from_url("http://www.kcgcollege.ac.in/index.shtml")
#end = time.time()
#print end - start
#for x in first_sublink:
#    for y in x:
#        print y
#for l in test_links:
#    print l
url1 = "http://www.kcgcollege.ac.in"
url2 = "http://www.stackoverflow.com"
url3 = "http://www.codeproject.com"
print "\n\n\n\n\n"

print test_links[0]
get_links_from_url(test_links[0])
test_links2 = queue.get()
write_into_row_csv_reduhandler(test_links2)



#for key, val in shtml.items():
#    print key, "  ", val
"""
urls = test_links[0]
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
            write_into_row_csv_reduhandler(t)
#    for x in t:
#        for y in x:
#            print y
#        print "\n\n\n\n\n\n"
"""







