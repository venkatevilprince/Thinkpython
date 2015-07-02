from four_1 import *
import math
from swampy.TurtleWorld import *
World = TurtleWorld()
bob = Turtle()
print bob
bob.delay = .001


def draw_triangle(t, lenth, angle):
    y = lenth * math.sin(angle / 2 * math.pi / 180)
    rt(t, angle / 2)
    fd(t, lenth)
    lt(t, 90 + angle / 2)
    fd(t, 2 * y)
    lt(t, 90 + angle / 2)
    fd(t, len)
    lt(t, 180 - angle / 2)
#draw_triangle(bob,100,60)


def draw_shape(t, lenth, n):
    angle = 360.0 / n
    for i in range(n):
        draw_triangle(t, lenth, angle)
        lt(t, 360.0 / n)
draw_shape(bob, 100, 9)
die(bob)
wait_for_user()
