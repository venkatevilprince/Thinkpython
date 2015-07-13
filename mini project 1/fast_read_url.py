import requests
import time
start = time.time()
link = "http://www.stackoverflow.com"
f = requests.get(link)
end = time.time()
print end - start
#print f.text
