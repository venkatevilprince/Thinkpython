import urllib2
import csv
import threading
import Queue
import time
import requests
import os

queue = Queue.Queue()
test_url = "http://www.srmuniv.ac.in/index.html"
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


get_links_from_url(test_url)
test_links = queue.get()

write_into_row_csv_reduhandler(test_links)
