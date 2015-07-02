import random

def sort_by_length(words):

    """ sorts with 2 argument tuple"""
    
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    print t
    res = []
    for length, word in t:
        print length,word
        res.append(word)
    return res


def sort_by_length_random(words):

    """ sorts with 3 argument tuple (length,random priority,word)"""
    
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)
    #print t
    res = []
    for length, _, word in t:
        print length,_,word
        res.append(word)
    return res

test=['a','b','c','ab','bc','aav','accc','ddda']

print sort_by_length_random(test)




