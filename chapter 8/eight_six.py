from eight_four import *

def letter_count_modified(word,letter):

    """ a modified count function which used the find function from eight-four"""
    
    index=-1;count=0
    for i in range(len(word)):
        index=find(word,letter,index+1)
        
        if(index!=-1):
            count=count+1
        else:
            break
        
    return count

print letter_count_modified("ppppython",'p')
