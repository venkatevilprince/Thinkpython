import urllib2
import urllib3
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
http = urllib3.PoolManager()

#functions

def get_url_data(web_url):

    try:
        start = time.time()
        #conn = requests.get(web_url)
        r = http.request('GET',web_url )
        #r = urllib2.urlopen(web_url)
        conn = r.data
        #print conn
        end = time.time()
        print end - start
        queue.put((web_url,conn))
    except urllib3.exceptions.InsecurePlatformWarning:
        print "platform exception"
    except urllib3.exceptions.InsecureRequestWarning:
    except:
        print "exception"
        pass

def get_links_from_url(data,web_url):
    #print web_url
    linklist = []
    tag="a href=\""
    endtag="\""
    for item in data.split('<'):
        #print item
        if "a href" in item:
            #print item
            
            try:
                ind = item.index(tag)
                #print ind
                item=item[ind+len(tag):]
                endt=item.index(endtag)
                link = item[:endt]
                #print link
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
shelfr = shelve.open("url.db",'c')
shelfr.close()
get_url_data(test_url)
test_url,get_conn = queue.get()
test_links = get_links_from_url(get_conn,test_url)
create_reader_dict()
write_into_row_csv_reduhandler(test_links)

urls = test_links
allthreads = []
response_list = []

def thread_control(urls):
    t_urls = []
    t_count = 16
    index = 0
    while index < len(urls):
        threads = []
        while t_count > 0 and index < len(urls):
            shelfr = shelve.open("url.db")
            if urls[index] not in shelfr.keys():
                print index
                t = threading.Thread(target=get_url_data, args=(urls[index],))
                threads.append(t)
                allthreads.append(t)
                t.start()
                t_count -= 1
            else:
                print "skipped"
            index += 1
            shelfr.close()
        print threads
        for t1 in threads:
            t1.join()
            t_count += 1

    return
thread_control(urls)
print "hahah"
for t in allthreads:
    t_url,t_data = queue.get()
    t_lists = get_links_from_url(t_data,t_url)
    response_list.append(t_lists)
    write_into_row_csv_reduhandler(t_lists)
    shelfw = shelve.open("url.db", 'c')
    shelfw[t_url] = t_url
    shelfw.close()



