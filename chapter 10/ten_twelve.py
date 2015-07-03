from ten_eleven import *
data = read_words()


def find_reverse(data):
    """prints words that can be formed by reversing a word"""
    for a in data:
        t = bisect(data, a[::-1])
        if(t):
            print a,
            for i in range(10 - len(a)):
                print "",
            print t
find_reverse(data)
