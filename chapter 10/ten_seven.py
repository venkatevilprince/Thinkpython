def is_anagram(word1, word2):
    """Returns True of the words are anagrams"""
    if len(word1) != len(word2):
        return False
    a=''.join(sorted(word1))
    #print a
    b=''.join(sorted(word2))
    #print b
    if  a == b:
        return True
    else:
        return False
test1 = "abngela"
test2 = "gleanab"
print is_anagram(test1, test2)
