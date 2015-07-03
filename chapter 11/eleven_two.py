def histogram(word):
    h = {}
    """ Returns the occurances of letters as a dictionary"""
    #print word
    for letter in word:
        if letter in h.keys():
            h[letter] += 1
        else:
            h[letter] = 1
    return h
if __name__ == "__main__":
    s = raw_input("enter a word")
    if(s.isalpha()):
        a = histogram(s.lower())
    else:
        print"wrong"
    print a
#print h.get('c',10)
#print h['a']
#a='z'
#print ord(a)-96
