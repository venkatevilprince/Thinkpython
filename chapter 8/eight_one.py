def reverse_print(word):
    
    """prints a word in reverse one per line"""
    
    for i in range(len(word)):
        print word[len(word)-1-i]


reverse_print("hello")        
        
