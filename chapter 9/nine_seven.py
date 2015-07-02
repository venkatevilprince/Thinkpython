def is_sequence(word):
    """ Returns True if the word contains three consecutive pairs
        of letters otherwise False"""
    count = 0; i = 0
    while i < (len(word) - 1):    
        if(word[i] == word[i + 1]):
            count += 1
            i = i + 2
            if(count == 3):
                return True
        else:
            i = i + 1
            count = 0
    return False
wordcount = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    """how many words have three consecutive pairs of letters"""
    if is_sequence(word):
        print word
        wordcount += 1
print is_sequence("aabaabbcc")  #Test Statement
print wordcount
