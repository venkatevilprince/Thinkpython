import os
import shelve
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 12'))
sys.path.append(path)
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)
from twelve_four import *#python import path set
from ten_ten import *
current =os.path.dirname(__file__)
chapter10 = os.path.normpath(os.path.join(path, '../chapter 10'))
#print chapter10
os.chdir(chapter10)  # python file path set to chapter 10
data = read_words()     
os.chdir(current)  #python file path set back to current to read other text files
anag_dict = all_anagrams(data)


def valid_anag(box):
    """Returns a lis of all valid anagrams i.e with minimum of two valid words"""
    t = []
    for val in box.values():
        if(len(val) > 1):
            t.append((len(val), val))
    t.sort(reverse=True)
    return t
anag_list = valid_anag(anag_dict)


def store_anag(item, filname):
    """Stores anagrams in a dictionary using Shelve"""
    shelf = shelve.open(filname, 'c')
    for key,val in item:
        s = "".join(sorted(val[0]))
        #print s
        shelf[s] = val
    shelf.close()        


def read_anag(word,filname):
    """Returns a lit of all the anagrams of the word including the word if the word
       is present in dictionary otherwise returns False"""
    shelf = shelve.open(filname)
    #for key, val in shelf.items():
    #   print key, val
    s="".join(sorted(word))
    if s in shelf.keys():
       #print word
       return shelf[s]
    return False


#store_anag(anag_list, "anagdict.db")
#print signature("123")
print read_anag("angel", "anagdict.db")

