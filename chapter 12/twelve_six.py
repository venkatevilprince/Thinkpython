import sys
import os
from ten_ten import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)
from ten_eleven import *
data = read_words()
#print bisect(data, "i")
count = 0
mem = {}
mem[''] = ['']
"""This program is so kool and it took hours to understand the recursions
   even with the solution"""


def make_dict(data):
    """creates adictionary with key = val and including a,i,and '' """
    box={}
    for l in data:
        a = l.strip().lower()
        box[a] = a
    for letter in ['a', 'i', '']:
        box[letter] = letter
    return box
word='sprite'
"""def word_reduce(data, word):
    global count
    count += 1
    #print count
    for i in range(len(word)):
        t=[]
        for l in word:
            t.append(l)
        del t[i]
        #print t
        rword="".join(t)
        if(not len(t)):
            print count
            count=0
        #print rword
        if bisect(data, rword):
            print rword
            word_reduce(data, rword)
"""


def is_reductible(box,word):
    """Returns the list of words tat can be reduced to '' """
    if word in mem:
        return mem[word]
    #print word
    res=[]
    #print children(box, word)
    for child in children(box, word):
        #print child
        t = is_reductible(box, child)
        #print t,"a",
        if(t):
            res.append(child)
            #print res,len(word)
    mem[word] = res
    #print res
    return res


def print_trail(word):
    """ prints the first combination that reduces the word to '' """
    if len(word) != 0:
        print word,
        
        t=is_reductible(box, word)
        print_trail(t[0])
        


def children(box, word):
    """Returns list of possible words after removing a letter """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i + 1:]
        if child in box:
            res.append(child)
    return res


def reduce_all(box):
    """Returns all the words in dictionary that reduuces to '' atleast in one way"""
    res = []
    for word in box:
        t = is_reductible(box,word)
        if t != []:
            res.append(word)
            #print word
    return res


def longest_reduce(box):
    """prints the first five longest words that reduce to '' """
    all = reduce_all(box)
    res = []
    for word in all:
        res.append((len(word), word))
    res.sort(reverse=True)
    for x,y in res[0:5]:
        print_trail(y)
        print '\n'   
box = make_dict(data)
#word_reduce(data, word)
#print children(box,"sprite")
print is_reductible(box, "tent")
#print_trail("sprite")
longest_reduce(box)

