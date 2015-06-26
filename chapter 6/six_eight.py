def gcd(a,b):
    """a simple GCD function for understanding recursion and
       determining the base case for recursion"""
    
    if(b==0):
        return a
    else:
        r=a%b
        return gcd(b,r)



print gcd(60,70)    
    
