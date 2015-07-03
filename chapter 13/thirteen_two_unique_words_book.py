import string
#print string.punctuation
def read_and_count(txtfile):
    with open(txtfile) as f:
        data = f.read()
    box = {}    
    #print data    
    for word in data.split():
        word = word.lower()
        s = ""
        for letter in word:
            if letter not in string.punctuation:
                s += letter
        #print s        
        if s in box:
            box[s] += 1
        else:
            box[s] = 1
    return box


def view_words(box):
    for x in sorted(box.keys()):
        print x, "  ", box[x]


def count_unique(box):
    count = 0
    for x in box.keys():
        count += 1
    return count
if __name__ == "__main__":
    book1 = "Catching Fire"
    bookwords1 = read_and_count(book1+".txt")
    book2 = "The Hunger Games"
    bookwords2 = read_and_count(book2+".txt")
    book1_vocabulary = count_unique(bookwords1)
    book2_vocabulary = count_unique(bookwords2)
    print book1, "contains", book1_vocabulary, "unique words"
    print book2, "contains", book2_vocabulary, "unique words"
        
