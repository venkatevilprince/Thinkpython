def capitalise_nested(list1):
    """Returns the capitalised nested list"""
    a = []
    for i in range(len(list1)):        
        if isinstance(list1[i], list):
            #print"1"
            a.append(capitalise_nested(list1[i]))
        else:
            #print "2"
            a.append(list1[i].capitalize())
    return a
test_list=['a', 'b' ,['c' ,['d' ,'e' ,'f'], 'g'], 'h', 'i']
print capitalise_nested(test_list)
#print test_list[0].capitalize()
