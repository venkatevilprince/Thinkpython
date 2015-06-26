def do_twice(f,g):
    f(g)
    f(g)
def print_twice(word):
    print word
print "prints twice"    
do_twice(print_twice,"spam")

def do_four(x,y):
    do_twice(x,y)
    do_twice(x,y)
print "prints four times"
do_four(print_twice,"spam")    
