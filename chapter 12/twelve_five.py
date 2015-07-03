from ten_ten import *
from twelve_four import *
data = read_words()


def metapairs(box):
    for l in box:
        for i in range(len(box[l]) - 1):
            if word_diff(box[l][i], box[l][i + 1]) == 2:
                print box[l][i],box[l][i + 1]   
box = all_anagrams(data)
word1 = "conserve"
word2 = "converse"
print zip(word1, word2)


def word_diff(word1, word2):
    t=[]
    count=0
    t=zip(word1, word2)
    for x, y in t:
        if x != y:
            count += 1
    return count        
print word_diff(word1, word2)
print metapairs(box)

    
