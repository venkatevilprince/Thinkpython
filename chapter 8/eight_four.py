def find(word, letter, index):
    """ returns the first index of the letter in a word
        Third parameter is the start index"""
    #index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

if __name__ == '__main__':
    print find("apple", 'p', 0)
