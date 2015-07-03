import string
print string.punctuation
with open("content.txt") as f:
    data = f.read()
print data    
for word in data.split():
    word = word.lower()
    s = ""
    for letter in word:
        if letter not in string.punctuation:
            s += letter
    print s        
