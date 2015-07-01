from eleven_two import *

def invert_dict(a):
    inv={}

    """ Returns a reversed dictionary"""
    
    for key,val in a.items():
        print val," ",key
        if val not in inv.keys():
            inv[val]=[key]
        else:
            inv[val].append(key)
        

    return inv    

    


def invert_dict2(a):

    """Returns a reversed dictionary with set default"""
    inv={}

    for key,val in a.items():
        inv.setdefault(val,[])
        inv[val].append(key)
        

    return inv 



s="apple"
a=histogram(s)
print a
print invert_dict2(a)
    

