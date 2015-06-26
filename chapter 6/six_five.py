def ack(m,n):
    
    """ this program taught me about maximum
        recursion depth
        if i try larger values it thorws an exception"""
    
    if(m==0):
        return n+1
    if(n==0 and m>0):
        return ack(m-1,1)
    if(n>0 and m>0):
        return ack(m-1,ack(m,n-1))


print ack(3,4)

    
