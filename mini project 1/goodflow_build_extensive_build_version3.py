from bs4 import BeautifulSoup
import unicodedata
import urllib2
import urllib3
import csv
import threading
import Queue
import time
import requests
import os
import shelve

# dictionaries
label_url_dict = {}

queue = Queue.Queue()
requests.packages.urllib3.disable_warnings()

def get_url_data(web_url):
    """gets the url data from a website url and puts it in a queue"""
    if "http" not in web_url:
        web_url = "http://"+ web_url
    try:
        start = time.time()
        conn = requests.get(web_url)
        c = conn.content
        end = time.time()
        print end - start
        time_con = end - start
        #if time_con > 6:
        #    print web_url
        queue.put((web_url,c))
    except urllib3.exceptions.InsecurePlatformWarning as e:
        print "InsecurePlatformWarning"
    except urllib3.exceptions.InsecureRequestWarning as f:
        print "InsecureRequestWarning"
    except:
        print "exception"
        print web_url
        queue.put((web_url,None))
        return

def create_reader_dict(filename):
    with open('{}.csv'.format(filename), 'r') as read_label_url:
        url_reader = csv.reader(read_label_url, delimiter=',', quotechar='\"')
        for row in url_reader:
            collegename,label,url = tuple(row)
            label_url_dict[url] = label
            

def get_label_url(data, college_url, csvname):
    soup = BeautifulSoup(data, "lxml")
    label_url = []
    local_dict = {}
    for link in soup.find_all('a'):
        url = link.get('href')
        label = goodtext(link.get_text().strip())
        #print len(label)
        if len(label) > 0 and url != None  and '#' not in url  :
            if 'http' not in url:
                url = "http://" + college_url + '/' +url 
            #print url
            #print label
            label_url.append((label,url))
            if url not in label_url_dict.keys():
                
                with open('{}.csv'.format(csvname), 'a') as write_label_url:
                    url_writer = csv.writer(write_label_url,delimiter=',',lineterminator='\n',
                            quotechar='\"', quoting=csv.QUOTE_NONE)
                    try:
                        url_writer.writerow((college_url,label,url))
                    except:
                        #strlabel = label.strip()
                        #print strlabel
                        pass
                        #strlabel = strlabel.encode("utf-8")
                        #print type(strlabel),strlabel
                        #url_writer.writerow((strlabel,url))
                label_url_dict[url] = label             
    return label_url

def goodtext(word):
    new_word = word.replace("-", "")
    return " ".join(new_word.split())

def striphttp(url):
    new = url.replace("http://","")
    return new
    
def website_scanner(college_url, filename):
    with open('{}.csv'.format(college_list), 'a') as fil_create:
        print "created"
    shelfr = shelve.open('{}.db'.format(filename), 'c')
    shelfr.close()
    create_reader_dict(filename)
    get_url_data(college_url)
    test_url,web_data = queue.get()
    first_list = get_label_url(web_data, college_url, filename)
    thread_control(first_list, college_url, filename)
    

def thread_control(urls, college_url,filename):
    allthreads = []
    t_urls = []
    t_count = 32
    index = 0
    global no_of_exceptions
    while index < len(urls):
        threads = []
        while t_count > 0 and index < len(urls):
            shelfr = shelve.open('{}.db'.format(filename))
            label,url = tuple(urls[index])
            if url not in shelfr.keys():
                print index
                if 'pdf' not in url:
                    t = threading.Thread(target=get_url_data, args=(url,))
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
            t1.join(5.0)
            t_count += 1
            t_url,t_data = queue.get()
            if t_data:
                t_lists = get_label_url(t_data,college_url,filename)
                shelfw = shelve.open("{}.db".format(filename), 'c')
                shelfw[t_url] = 'present'
                shelfw.close()
    return
#test codes
#parent = "www.srmuniv.ac.in"
#parent2 = "www.kcgcollege.ac.in"
#website_scanner(parent)
#website_scanner(parent2)

college_list = "collegelist"

try:
    with open(college_list+".txt", 'r') as fin:
        fin_data = fin.read()
        for line in fin_data.split():
            line = line.strip()
            if 'http://' in line:
                line = line.strip("http://")
            print line
            try:
                test = requests.get("http://" + line)
                #print "success"
                website_scanner(line, college_list)
            except:
                print "website error"
except:
    print " error opening file "
        


    #if len(label) == 0 and url != None:
    #    
    #    print link.get('href')
    #    print link.findAll('img')[0].get('src')
    #    #print link.get('src')

print "END"


