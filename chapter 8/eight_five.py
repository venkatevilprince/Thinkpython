def letter_count(word, letter):
    """count the number of occurance of a letter in word"""
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    return count
print letter_count("apple",'p')
