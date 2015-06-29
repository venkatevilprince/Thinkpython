"""reads all the words from the text file and prints
   the words which has more than 20 characters"""


fin = open('words.txt')
for line in fin:
    word = line.strip()
    if(len(word)>=20):
        print word

    
