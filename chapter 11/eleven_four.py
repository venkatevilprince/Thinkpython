from eleven_two import *


def reverse_lookup(a, n):
    """ Returns a list of keys for a given dictionary value """
    l = []
    for key, val in a.items():
        if(val == n):
            #print val," ",key
            l.append(key)
    return l
s = "apple"
a = histogram(s)

print 1, " : ", reverse_lookup(a, 1)
