from ten_ten import *
from eight_twelve import*
from ten_eleven import *
data=read_words()
box={}

def is_rotate(data):

    """ Prints valid words from all possible rotations of each word
        in words.txt and stores them in a dictionary """
    
    s1=10;s2=10
    for i in range(len(data)):

        for j in range(1,26):

            t=bisect(data,rotate_word(data[i],j))
            if(t):
                box[data[i]]=t
                print data[i],
                for x in range(10-len(data[i])):
                    print "",
                print j,    
                for y in range(10-len(str(j))):
                    print "",
                print t



is_rotate(data)

