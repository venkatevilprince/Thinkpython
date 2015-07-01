from ten_ten import *
import time

""" Prints Time taken by the in statement to find a value"""

words={}
data=read_words()

for i in range(len(data)):
    words[i]=data[i]

find="catapult"

start=time.time()

#print words 

if "apple" in words.values():
    #print key,val
    #if(val==find):
    print"true"
    
    
        
        

end=time.time()

print end-start




