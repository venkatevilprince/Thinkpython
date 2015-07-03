from thirteen_two_unique_words_book import *


def most_frequent(box,n):
    res = []
    for x, y in box.items():
        res.append((y,x))
    res.sort(reverse=True)
    for x, y in res[0:n]:
        print x, y
    return res
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookhist1 = read_and_count(book1 + ".txt")
    book2 = "The Hunger Games"
    bookhist2 = read_and_count(book2 + ".txt")
    print book1
    booklist1 = most_frequent(bookhist1, 20)
    print book2
    booklist2 = most_frequent(bookhist2,2 0)
    
