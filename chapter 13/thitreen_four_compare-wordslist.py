import os
import sys
from thirteen_two_unique_words_book import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)
from ten_ten import *   #python import path set
current=os.path.dirname(__file__)
chapter10=os.path.normpath(os.path.join(path, '../chapter 10'))
#print chapter10
os.chdir(chapter10)  # python file path set to chapter 10
data=read_words()     
os.chdir(current)  #python file path set back to current to read other text files


def typo_words(box):
    """ prints all the typo words and returns a list of the words"""
    res=[]
    count=0
    total=0
    for x in box.keys():
        total+=1
        if x not in data:
            print x
            count+=1
            res.append(x)
    return res,count,total
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookhist1 = read_and_count(book1+".txt")
    book2 = "The Hunger Games"
    bookhist2 = read_and_count(book2+".txt")
    typo1, no_words, total = typo_words(bookhist1)
    print no_words, "are typo words out of",total, "words"
