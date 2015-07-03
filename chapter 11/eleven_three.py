from eleven_two import *


def print_hist(a):
    for i in sorted(a):
        print i, " ", a[i]
s = "apple"
a = histogram(s)
print_hist(a)
