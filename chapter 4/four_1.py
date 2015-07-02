import math
from swampy.TurtleWorld import *
#square code t is turle and len is length


def square(t, len):
    for a in range(4):
        fd(t, len)
        rt(t)
#square(bob,100)
#polygon code t-turtle, len-length of sides,n-number of sides


def polygon(t, len, n):
    for a in range(n):
        fd(t, len)
        rt(t, (360.0 / n))
#polygon(bob,100,5)


#circle code t-turtle and r-radius of circle
def circle(t, r):
    n = 20.0
    len = (2 * 3.14 * r) / n
    for a in range(n):
        fd(t, len)
        rt(t, (360.0 / n))
#circle(bob,50)


#arc code t-turtle, r-radius, angle is angle subtended
def rarc(t, r, angle):
    n = 360.0
    steplen = 360.0 / n
    len = (2 * 3.14 * r) / n
    n = math.floor((angle / 360.0) * n)
    n = int(n)
    for a in range(n):
        fd(t, len)
        rt(t, steplen)


def larc(t, r, angle):
    n = 360.0
    steplen = 360.0 / n
    len = (2 * 3.14 * r) / n
    n = math.floor((angle / 360.0) * n)
    n = int(n)
    for a in range(n):
        fd(t, len)
        lt(t, steplen)
if __name__ == '__main__':
    World = TurtleWorld()
    bob = Turtle()
    print bob
    bob.delay = .001
    larc(bob, 50, 90)
    die(bob)
    wait_for_user()
