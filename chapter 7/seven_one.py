import time
def countdown(n):
    
    """counts down by seconds and when it expites it blastsoff
       This is for understanding loops"""

    for i in range(n):
        print n-i
        time.sleep(1)
    print 'Blastoff!'

countdown(10)





        
