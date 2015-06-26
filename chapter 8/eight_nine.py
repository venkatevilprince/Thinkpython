def is_reverse(word1,word2):
        
        """Checks whether the two word are the exact reverse of each other"""
        
        if len(word1) != len(word2):
            return False
        i = 0
        j = len(word2)-1
        while j >= 0:
            print i, j # print here
            if word1[i] != word2[j]:
                return False
            i = i+1
            j = j-1
        return True

print is_reverse('stop','pots')
       
