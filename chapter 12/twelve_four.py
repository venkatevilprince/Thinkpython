from ten_ten import *
data = read_words()


def sorts(word):
    a = ''.join(sorted(word))
    return a
"""  This one is too slow
def all_anagrams(data):
    for i in range(len(data)):
        #print i
        if(not sorts(data[i]) in box):
            for j in range(len(data)):
                if sorts(data[i])==sorts(data[j]):
                   if sorts(data[j]) in box:
                        box[sorts(data[i])].append(data[j])
                   else:    
                        box[sorts(data[i])]=[]
"""


def all_anagrams(data):
    """Returns a dictionary of all possible anagrams"""
    box = {}

    for i in range(len(data)):
        #print i
        s = sorts(data[i])

        if s in box:
            box[s].append(data[i])
        else:
            box[s] = [data[i]]
    return box        


def order(box):
    """returns an reverse ordered list of tuple (length,anagrams) """   
    t = []
    for val in box.values():
        if(len(val) > 1):
            t.append((len(val), val))
    t.sort(reverse=True)        
    for x in t:
        print x
    return t        


def ret_len(box, n):
    """returns a dictionary with only eight letter words"""
    t = {}
    for x, y in box.items():
        if(len(x) == n):
            t[x] = y
    #for x in t:
        #print x
    return t        
test = "dcba"
#print sorts(test)
crate = all_anagrams(data)
#ordered=order(crate)
eight = ret_len(crate, 8)
order(eight)
print "a"
