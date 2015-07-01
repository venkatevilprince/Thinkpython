def remove_duplicates(item):

    """ I did this in a hard way so that i dont have to
        affect the order of items """
    
    for i in range(len(item)):
        #print len(item)
        #print i
        for j in range(len(item)):

            #print j
            #print len(item)
            if item[i] == item[j] and i!= j:
                item[j]=" "
                
                #print item
    #print item
    dc=0
    for i in range(len(item)):
        if item[i]==" ":
            dc+=1
    for i in range(dc):
        item.remove(" ")
    return item

def remove_duplicates_easy(item):

    """This is what the book wanted"""
    
    a=item[:];a.sort()
    a.append(' ')
    r=[]
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
           r.append(a[i])
    return r       
           


test=[1,8,9,3,3,4,5,6,1,2,3,4,5,1,2,3,4,6,6,7,8,3,6,8,6]

print remove_duplicates(test)

print remove_duplicates_easy(test)

    
