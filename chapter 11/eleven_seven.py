mem={}

import time

def ack(m,n):
    
    """ this program taught me about try and exception

        Prints all the memorised vaues"""
    
    if(m==0):
        return n+1
    if(n==0 and m>0):
        return ack(m-1,1)
    

    try:
        return mem[m,n]
    except KeyError:
        mem[m,n]=ack( m-1,ack(m,n-1))
        return mem[m,n]

print ack(3,4)
print ack(1,344)
print mem 
