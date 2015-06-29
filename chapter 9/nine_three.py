def avoids(word,forbidden_letters):
    
    """Returns True if the word does not contain any
       letter from the forbidden word"""

    for letter in word:
        for fl in forbidden_letters:
            if(letter==fl):
                return False
    return True
            

totalwords=0    
wordcount=0
user_input=raw_input("Enter the forbidden Letters as a word\"(example aeiou)\"")
fin = open('words.txt')        
for line in fin:
    word = line.strip()
    totalwords+=1
    if(avoids(word,user_input)):
        wordcount+=1

print "{} words in the file words.txt does not have the letter {}".format(wordcount,user_input) 
#print totalwords 
