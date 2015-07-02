from swampy.TurtleWorld import *
World = TurtleWorld()
bob = Turtle()
print bob
bob.delay = .0001


def koch(t, order, length):
    """this made me clearly understand the recursive functions"""
    if order == 0:
        fd(t, length)
    else:
        koch(t, order-1, length/3)
        lt(t, 60)
        koch(t, order-1, length/3)
        rt(t, 120)
        koch(t, order-1, length/3)
        lt(t, 60)
        koch(t, order-1, length/3)


def snowflakes(t, order, length):
    for i in range(3):
        koch(t, order, length)
        rt(t, 120)
snowflakes(bob, 5, 300)
die(bob)
wait_for_user()
