import string
my_punc = string.punctuation + "1234567890"


#print data    

def strip_punc(word):
    """Strips punctuations from the word and returns the word"""

    word = word.lower()
    #print word
    s = ""
    for letter in word:
        if letter not in my_punc:
            s += letter
    return s
    
if __name__ == "__main__":
    with open("content.txt") as f:
        data = f.read()
    for word in data.split():
        s = strip_punc(word)
        if(s):
            print s
