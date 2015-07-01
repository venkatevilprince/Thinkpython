from ten_ten import *
import time

def bisect(item,find):

    """ Returns the word if it finds otherwise false
        uning binary search algorithm """
    
    first=0;last=len(item)-1;
    mid=(first+last)/2
    found=False

    while first<=last and not found:
        mid=(first+last)//2
        if(find==item[mid]):
            found=item[mid]
            #print item[mid]
        else:
            
            if item[mid]>find:
                last=mid-1
                #print item[mid]
            else:
                first=mid+1
                #print item[mid]
        
        

        #print first   

    return found


if __name__=="__main__":
    find="catapult"    
    data=read_words()
    #data=[2,2,2,2,4,5,6,7]
    start=time.time()
    print bisect(data,find)
    end=time.time()
    print end-start

    

    #print "aa">"aaaa"
