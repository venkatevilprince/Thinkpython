import os
import random
import sys
from thirteen_two_unique_words_book import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 10'))
sys.path.append(path)
from ten_eleven import *   #python import path set
current =os.path.dirname(__file__)
chapter10 = os.path.normpath(os.path.join(path, '../chapter 10'))
#print chapter10
os.chdir(chapter10)  # python file path set to chapter 10
data = read_words()     
os.chdir(current)  #python file path set back to current to read other text file


def random_words(box):
    """returns the word if the random number matches the cumilative frequency list"""
    word = []
    freq = []
    cum_freq = 0
    for x,y in box.items():
        cum_freq = cum_freq + y
        freq.append(cum_freq)
        word.append(x)

    x = random.randint(0, cum_freq-1)
    index = bisect(freq,x)
    #print index
    return word[index]
   
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookhist1 = read_and_count(book1+".txt")
    book2 = "The Hunger Games"
    bookhist2 = read_and_count(book2+".txt")
    for i in range(100):    #prints some random words
        print random_words(bookhist1),
    
