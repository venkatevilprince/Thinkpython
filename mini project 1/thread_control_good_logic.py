import urllib2
import csv
import threading
import Queue
import time
import requests
import os
import shelve
#queues
queue = Queue.Queue()
#dictionaries
univ_dict = {}
reader_dict = {}
url_dict = {}

#functions

def get_url_data(web_url):
    start = time.time()
    conn = requests.get(web_url)
    end = time.time()
    print end - start
    queue.put((web_url,conn))

def get_links_from_url(data,web_url):
    #print web_url
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
    return linklist

def create_reader_dict():
    readlinks = open("links.csv", 'r')
    reader = csv.reader(readlinks, delimiter=',', quotechar='\"')
    for row in reader:
        for r in row:
            if r not in reader_dict.keys():
                reader_dict[r] = r
    readlinks.close()

def write_into_row_csv_reduhandler(url_list):
    with open('links.csv', 'a') as links:
            spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        
            no_redundancy = []
            for url in url_list:
                #print url
                if len(url) > 0:
                    if url not in reader_dict.keys():
                        #print url
                        no_redundancy.append(url)

            #no_redundancy.append(url)
            if(len(no_redundancy)>0):
                spamwriter.writerow(no_redundancy)


#test codes
test_url = "http://www.srmuniv.ac.in/index.html"          
with open('links.csv', 'a') as fil_create:
    print "created"
get_url_data(test_url)
test_url,get_conn = queue.get()
test_links = get_links_from_url(get_conn,test_url)
create_reader_dict()
write_into_row_csv_reduhandler(test_links)

urls = test_links[0:13]
threads = []
response_list = []

def thread_control(urls):
    t_urls = []
    t_count = 8
    index = 0
    while index < len(urls):
        threads = []
        while t_count > 0 and index < len(urls):
            print index
            #print t_count
            #print urls[index]
            t = threading.Thread(target=get_url_data, args=(urls[index],))
            threads.append(t)
            t.start()
            index += 1
            t_count -= 1
        print threads
        for t1 in threads:
            t1.join()
            t_count += 1
            t_url,t_data = queue.get()
            #print "got",t_url
    return
thread_control(urls)
print "hahah"






