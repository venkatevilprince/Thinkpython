import urllib2
import csv
import threading
import Queue
import time
import requests
import os
import shelve

queue = Queue.Queue()

test_url = "http://www.srmuniv.ac.in/index.html"
univ_dict = {}
reader_dict = {}
url_dict = {}
threadLimiter = threading.BoundedSemaphore(12)

class EncodeThread(threading.Thread):

    def run(self,urls):
        threadLimiter.acquire()
        try:
            for url in urls:
                shelfr = shelve.open("url.db")
                if url not in shelfr.keys():
                    print url
                    t = threading.Thread(target=get_url_data, args=(url,))
                    threads.append(t)
                    t.start()
        finally:
            threadLimiter.release()


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

def write_into_row_csv(url_list):
    with open('links.csv', 'a') as links:
        spamwriter = csv.writer(links,delimiter=',',lineterminator='\n',
                            quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(url_list)

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


with open('links.csv', 'a') as links:
    print "created"
get_url_data(test_url)
test_url,get_conn = queue.get()
test_links = get_links_from_url(get_conn,test_url)
create_reader_dict()
write_into_row_csv_reduhandler(test_links)


url1 = "http://www.kcgcollege.ac.in"
url2 = "http://www.stackoverflow.com"
url3 = "http://www.codeproject.com"
print "\n\n\n\n\n"


print len(test_links)
urls = test_links[0:23]
threads = []
response_list = []

#control = EncodeThread()
#control.run(urls)


def thread_control(urls):
    t_urls = []
    n=10
    print len(urls)
    for i in range(len(urls)/n):
        t_urls.append(urls[n*(i):n*(i+1)])
    t_urls.append(urls[(len(urls)/n)*n:len(urls)])
    print t_urls
    for a in t_urls:
        threads= []
        try:  
            for url in a:
                print "this happens"
                shelfr = shelve.open("url.db")
                if url not in shelfr.keys():
                    print url
                    t = threading.Thread(target=get_url_data, args=(url,))
                    threads.append(t)
                    t.start()
            for t in threads:
                print"happens"
                t.join()        # get results from thread
                t_url,t_data = queue.get()
                t_lists = get_links_from_url(t_data,t_url)
                response_list.append(t_lists)
                write_into_row_csv_reduhandler(t_lists)
                shelfw = shelve.open("url.db", 'c')
                shelfw[t_url] = t_url
                shelfw.close()
                shelfr.close()
    
        except:
            pass

    #t.urls.append(urls[(len(len(urls)/10)*10:len(urls))
    
        
thread_control(urls)
"""
for t in threads:
    t.join()        # get results from thread
    t_url,t_data = queue.get()
    t_lists = get_links_from_url(t_data,t_url)
    response_list.append(t_lists)
    write_into_row_csv_reduhandler(t_lists)
    shelfw = shelve.open("url.db", 'c')
    shelfw[t_url] = t_url
    
#for r in response_list:


"""




