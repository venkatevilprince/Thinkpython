from seven_two import *
import math


def test_square_root():
    """Prints the number, its square root in the math module,
       its square root from function in seven_two and the absolute
       difference between both like a table"""
    for i in range(1, 10):
        print("{0:.1f}".format(i)),
        print("{0:.11f}".format(math.sqrt(i))),
        print("{0:.11f}".format(square_root(float(i), 3))),
        print("{0:.11f}".format(square_root(float(i), 3) - math.sqrt(i)))
test_square_root()
