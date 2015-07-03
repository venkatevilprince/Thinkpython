from ten_eleven import *
data = read_words()


def can_interlock(data, word):
    """ Returns True if the word can be formed by interlocking valid words"""
    for i in range(len(word)):
        odd = word[::2]
        #print odd
        even = word[1::2]
        #print even
    return bisect(data, odd) and bisect(data, even)
#word="schooled"
#odd=word[::2]
#print odd
#even=word[1::2]
#print even


def can_interlock_gen(data, word, n):
    """ Returns True if the word can be formed by interlocking valid words
        Order of interlocking = n"""
    pat = []
    for i in range(n):
        pat.append(word[i::n])
        #print pat[i]
        if not bisect(data, pat[i]):
            return False
    return True
for i in range(len(data)):
    if can_interlock(data, data[i]):
        print data[i]
for i in range(len(data)):
    if can_interlock_gen(data, data[i], 3):
        print data[i]
