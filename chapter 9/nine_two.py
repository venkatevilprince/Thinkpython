def has_no_e(word):
    """ Returns True if the word does not have letter 'e'"""
    for letter in word:
            if(letter == 'e'):
                return False
    return True


def percentage_words(fin):
    """Reads the text file words.txt and Returns the
       total number of words that does not have the letter 'e' in it"""
    totalwords = 0
    word_without_e = 0
    for line in fin:
        word = line.strip()
        if(has_no_e(word)):
                word_without_e += 1
        totalwords += 1
    totalwords = float(totalwords)
    return (word_without_e / totalwords) * 100
fin = open('words.txt')
#print has_no_e("aaaa")
print "{0:.2f} % of words does not have the letter 'e'".format(percentage_words(fin))
