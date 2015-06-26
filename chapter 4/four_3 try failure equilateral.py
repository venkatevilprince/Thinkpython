from four_1 import *
import math
from swampy.TurtleWorld import *

World=TurtleWorld()
bob=Turtle()
print bob
bob.delay=.001



def draw_triangle(t,len):
    for i in range(3):
        fd(t,len)
        lt(t,180-60)

#draw_triangle(bob,100)

def draw_shape(t,len,n):
    for i in range(n):
        draw_triangle(t,len)
        lt(t,360.0/n)

draw_shape(bob,100,5)


wait_for_user()



    
