def is_abecederian(word):
    
    """ Returns True if the letters in a word
        appear in alphabetical order (double letters are ok)
        otherwise Flase"""
    
    for a in range(1,len(word)):
        if( not word[a-1]<=word[a]):
            return False
    return True

wordcount=0


fin = open('words.txt')        
for line in fin:
    word = line.strip()
    """how many words in word.txt is abecederian"""
    if is_abecederian(word):
        wordcount+=1


print is_abecederian("aabbccdd") #Test Statement
print wordcount
