import os
import sys
from thirteen_one_strippunc import * 
from thirteen_two_unique_words_book import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)  #python import path set
from ten_ten import *
chapter10 = os.path.normpath(os.path.join(path, '../chapter 10'))
current = os.path.dirname(__file__)
os.chdir(chapter10)  # python file path set to chapter 10
data = read_words()  #data is a dictionary of words.txt
os.chdir(current)  #python file path set back to current to read other text files


def typo_words_set(bookbox,wordbox):
    """ prints all the typo words(words that are not in the words.txt)
        and returns the list of the words"""
    res = []
    return set(bookbox)-set(wordbox)

test_dict1 = {'a': 1, 'b': 2, 'c': 3}
test_dict2 = {'c': 4, 'd': 5, 'e': 6}
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookhist1 = read_and_count(book1+".txt")  #bookhist is a dictionary of words in the book
    book2 = "The Hunger Games"
    bookhist2 = read_and_count(book2+".txt")
    typo1 = list(typo_words_set(bookhist1,data))
    for x in typo1:
        t=strip_punc(x)
        if(t):
            print t
        
    #typo1, no_words, total = typo_words_set(bookhist1)
    #print no_words, "are typo words out of", total, "words"
