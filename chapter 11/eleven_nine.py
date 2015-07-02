def has_duplicates(item):

    """Returns true if items has duplicate values"""
    
    for i in item:
        if i in box.keys():
            return True
        else:
            box[i]=1
    return False        


box={}


test=[1,2,3,4,5,7,6,3,3,4,5]


print has_duplicates(test)
print box
