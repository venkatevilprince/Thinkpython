def cumulative_sum(item):

    """Return the cumulative sum of the list passed"""
    
    a=[];
    for i in range(len(item)):
        sum=0
        for j in range(i+1):
            #print "a",
            sum=sum+item[j]
            #print sum
        print""
        #print sum
        a.append(sum)
            
        
    return a


test=[1,2,3,4,5]

print cumulative_sum(test)        
