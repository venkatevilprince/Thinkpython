univ={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',
      11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',
      21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
      
def rotate_word(word,rotation):
    
    """returns a rotate string by the value rotation using
       an universal dictionary"""
    
    new_word=""
    for char in word:
        for key,val in univ.items():
            if char in val:
                rotate=key+rotation
                if(rotate>26):
                    rotate=rotate%26
                if(rotate<0):
                    rotate=rotate%26
                    
                new_word=new_word+univ[rotate]
    return new_word            


print rotate_word("melon",42)




