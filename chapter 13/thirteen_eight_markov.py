from thirteen_one_strippunc import *
import random
import os
import sys
from thirteen_two_unique_words_book import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)
from ten_ten import *   #python import path set
current =os.path.dirname(__file__)
chapter10 = os.path.normpath(os.path.join(path, '../chapter 10'))
#print chapter10
os.chdir(chapter10)  # python file path set to chapter 10
data = read_words()     
os.chdir(current)  #python file path set back to current to read other text files
prefix=()
suffix_map = {}


def prefix_suffix(word, order = 2):
    """Creates a dictionary that maps set of prefixes of order n to possble suffixes"""
    global prefix
    if len(prefix)<order:
        prefix += (word,)
        return
    #print prefix
    try:
        suffix_map[prefix].append(word)  #Appending to the previous entry
    except KeyError:
       suffix_map[prefix] = [word]  #Adding new entry as list  
    prefix = shift(prefix, word)


def shift(t, word):
    """Shifting is done to consider the next set of prefix"""
    return t[1:]+ (word,)


def random_text(n = 100):
    """Generates a random text from the dictionary, suffix_maps"""
    start = random.choice(suffix_map.keys())
    for i in range(n):
        suffixes = suffix_map.get(start,None)
        if suffixes == None:  #exception handler for the                   
            print i           #last set of tuple which does not have suffix.
            random_text(n - i)
            return
        word = random.choice(suffixes)
        print word,
        start = shift(start, word)


def add_vocabulary(box,n):
    """Adds the words in the books to suffix_maps """
    for key in box.keys():
        #print s
        prefix_suffix(key ,n)
    
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookhist1 = read_and_count(book1+".txt")
    book2 = "The Hunger Games"
    bookhist2 = read_and_count(book2+".txt")
    n = 2
    add_vocabulary(bookhist1,n)
    add_vocabulary(bookhist2,n) 
    #for key in sorted(suffix_map.keys()):
        #print key
    random_text()
    #print prefix
