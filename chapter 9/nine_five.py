from nine_four import *


def uses_all(word, letters):
    """Returns True if the word uses all the characters in letters
       atleast once"""
    if(uses_only(word, letters)):
        if(uses_only(letters, word)):
            return True
        else:
            return False
    return False
wordcount = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    """how many words uses all the letters "aeiou

       Change the "aeiou" in the function parameter
       to check for other values"""
    if uses_all(word, "aeiou"):
        wordcount += 1
print uses_all("pills", "pils")  #test statement
print wordcount
