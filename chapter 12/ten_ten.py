import time


def read_words(s='words.txt'):

    """executes faster"""
    a=[]
    with open(s, 'r') as f:
        #read_data = f.read()
        #print read_data
        for b in f:
            #print b
            for w in b.split():
                a.append(w)

    return a

def read_words2():

    """takes almost 30 seconds to execute"""
    
    a=[]
    with open('words.txt', 'r') as f:
        #read_data = f.read()
        #print read_data
        for b in f:
            #print b
            for w in b.split():
                a=a+[w]

    return a

if __name__=="__main__":
    start = time.time()
    n=read_words()
    end = time.time()


    print end - start
    start = time.time()
    n=read_words2()
    end = time.time()

    print end - start
    print"done"





        
