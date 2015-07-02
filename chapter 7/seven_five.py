import math
"""
I have created two functions for calulating factorial
and i prefer iteration beacuse recursion consumes more memory"""


def factorial_recursion(n):
    """returns the factorial calculated through recursion"""
    if(n == 1):
        return 1
    else:
        return n * factorial_recursion(n - 1)


def factorial_iteration(n):
    """ returns factorial calculated through iteration"""
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def calculate_pi():
    """ Returns the approximate value of pi using formula derived by
        Mathematician Ramanujam"""
    sum = 0.0; k = 0.0; term = 10
    while(term > 1e-15):
        term = (factorial_iteration(int(4 * k)) * (1103 + 26390 * k)) / ((factorial_iteration(int(k)) ** 4) * (396 ** (4 * k)))
        sum = sum + term
        k = k + 1
    val = (sum * 2 * math.sqrt(2)) / 9801
    return 1 / val
print "factorial by recursion",
print factorial_recursion(6)
print "factorial by iteration",
print factorial_iteration(6)
print "Value of pi : {0:.30f}" .format(calculate_pi())


def is_palindrome(word):
    """ function checks if the i th element equals the
        (lenth-1-i) elemnet and even if it fails once it
        is not a palindrome """
    l = len(word)
    for i in range(l / 2 + 1):
        if(word[i] != word[l - 1 - i]):
            print "not a palindrome"
            return
    print "palindrome"
word = "redivider"
is_palindrome(word)
