import threading
import Queue
import time
queue = Queue.Queue()

def worker(num):
    """thread worker function"""
    time.sleep(5-num)
    print 'Worker: %s' % num
    
    queue.put(num)

threads = []
data = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)


thread_results = []
for thread in threads:
    #time.sleep(.0001)
    thread.start()
    

#Kill all threads
for thread in threads:
    response = queue.get()
    thread_results.append(response)
    thread.join()

print thread_results
