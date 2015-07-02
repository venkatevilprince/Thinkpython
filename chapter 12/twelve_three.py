
def most_frequent(word):

    """ Returns a list with letters sorted in reverse order of frequency"""
    
    t=[]
    h=make_histogram(word)

    for x,y in h.items():
        t.append((y,x))

    
    t.sort(reverse=True)
    #print t
    r=[]

    for x,y in t:
        r.append(y)
        
    return r
    
def make_histogram(s):

    """ returns a dictionary with histogram of the letter"""
    
    hist = {}
    for x in s:
        if x in hist.keys():
            hist[x]+=1
        else:
            hist[x]=1
    return hist




#test="aappplleeeq"

#print make_histogram(test)

#print most_frequent(test)
with open('words.txt','r') as f:
    s=f.read()

l=most_frequent(s)
del l[0]
print l
