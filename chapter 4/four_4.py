from four_1 import *
import math
from swampy.TurtleWorld import *
World = TurtleWorld()
bob = Turtle()
print bob
bob.delay = .0001
""" f-forward
    r-reverse
    l-left
    r-right
    ret-return with back"""


def fret(t, l):
    fd(t, l); pu(t)
    lt(t, 180); fd(t, l)
    lt(t, 180); pd(t)


def bret(t, l):
    lt(t, 180); fd(t, l); pu(t)
    lt(t, 180); fd(t, l); pd(t)


def lret(t, l):
    lt(t); fd(t, l); pu(t)
    lt(t, 180); fd(t, l); lt(t); pd(t)


def rret(t, l):
    rt(t); fd(t, l); pu(t)
    lt(t, 180); fd(t, l); rt(t); pd(t)


def diag(l):
    l = math.sqrt(2)*l
    return l


def mid(t, l):
    lt(t, 180)
    fd(t, l / 2)
    lt(t, 180)


def moveturtle(t):
    pu(t); fd(t, 120); pd(t)


def height(l):
    return l * math.sqrt(2) * math.sin((70.0 / 180) * 3.14)


def draw_a(t, size):
    lt(t, 70)
    dsize = diag(size)
    fd(t, dsize)
    rt(t, 180 - 40)
    fd(t, dsize)
    mid(t, dsize); rt(t, 180-70)
    fd(t, size / 2)
    lt(t, 70); pu(t)
    fd(t, dsize / 2); lt(t, 180-70)
    pd(t)


def draw_b(t, size):
    h = height(size)
    lret(t, h)
    larc(t, h / 4, 180); lt(t, 180)
    larc(t, h / 4, 180); pu(t)
    lt(t)
    fd(t, h); lt(t); pd(t)


def draw_c(t, size):
    pu(t)
    h = height(size)
    fd(t, h / 2); pd(t)
    lt(t, 180); rarc(t, h / 2, 180); pu(t)
    lt(t, 180); fd(t, h / 2); lt(t); fd(t, h); lt(t); pd(t)


def draw_d(t, size):
    h = height(size)
    lt(t); fd(t, h); rt(t); rarc(t, h / 2, 180)
    lt(t, 180)


def draw_e(t, size):
    h = height(size)
pu(bob)
lt(bob, 180)
fd(bob, 100)
lt(bob, 180)
pd(bob)
draw_a(bob, 100)
moveturtle(bob)
draw_b(bob, 100)
moveturtle(bob)
draw_c(bob, 100)
moveturtle(bob)
draw_d(bob, 100)
die(bob)
wait_for_user()
