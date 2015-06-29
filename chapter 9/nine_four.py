def check(singlechar,word):
    
    """Return True if the single character is present
       in the word otherwise false"""

    flag=0
    for letter in word:
        if(singlechar==letter):
            flag=1    
    if(flag==1):
        return True
    else:
        return False



def uses_only(word,letters):

    """Returns True if the word is formed only with the letters
       otherwise Flase"""

    for i in word:
        if(not check(i,letters)):
            return False
        
    return True
                
if __name__ == "__main__":
    print uses_only("pills","pils")
