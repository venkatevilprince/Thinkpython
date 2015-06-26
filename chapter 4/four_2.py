from four_1 import *
import math
from swampy.TurtleWorld import *



World=TurtleWorld()
bob=Turtle()
print bob
bob.delay=.001

def petal(t,r,ang):
    for i in range(2):
        rarc(t,r,ang)
        rt(t,180-ang)

def flower(t,n,r,ang):
    for i in range(n):
        petal(t,r,ang)
        lt(t,360.0/n)
    





flower(bob,100,1000,20)
die(bob)
wait_for_user()
