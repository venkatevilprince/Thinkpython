def is_reversed(val1,val2):

    """ returns True if both the values are exactly reverse"""
    
    if(val1%10 ==0):  #this statemnet handles exception like 10 and 01,20 and 02 
        val1=val1/10
    if(val2%10 ==0):
        val2=val2/10
        
    val1=str(val1)
    val2=str(val2)
    return val1==val2[::-1]

def howmany_times(val1,val2):
    
    """Returns how many times val1 and val2 are exactly reverse"""

    count=0
    i=0
    while i<99:
        #print val1+i,val2+i
        if(is_reversed(val1+i,val2+i)):
            count+=1
            #print "aaa"
        i+=1    
    return count


#print howmany_times(1,19)
"""LOOP thorusgh to find all the possibilities"""
print "POSSIBLE COMBINATIONS"
for i in range(1,99):
    for j in range(1,99):
        count=howmany_times(i,j)
        if(count==8 and i<j):
            print "child : {}  mother ; {}".format(i,j)
       
