

def is_palindrome(word):
    
    """ function checks if the i th element equals the
        (lenth-1-i) elemnet and even if it fails once it
        is not a palindrome """
    
    l=len(word)
    for i in range(l/2+1):
        if(word[i]!= word[l-1-i]):   
            print "not a palindrome"
            return
    print "palindrome"    

word="redivider"
is_palindrome(word)

