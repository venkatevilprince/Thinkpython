import copy
import sys
import os
from swampy.World import *

class point(object):
    """represents x and y coordinates"""
class rectangle(object):
    """Represents a rectangle

    attributes: width, height, corner"""


def print_coordinates_rec(rec):
    print "({}, {})".format(rec.corner.x,rec.corner.y)


def move_rectangle(rect,dx,dy):
    """move the rectange bu shifting the coordinates by dx and dy"""
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect


world = World()

def create_bbox(rect):
    p1 = []
    p1.append(-1 * (rect.width/2))
    p1.append(-1 * (rect.height/2))
    p2 = []
    p2.append( rect.width / 2)
    p2.append( rect.height / 2)
    box = []
    box.append(p1)
    box.append(p2)
    return box

def draw_rectangle(canvas,rect):

    bbox = create_bbox(rect)
    canvas.rectangle(bbox, outline='black', width=2, fill='red')


def create_canvas(world, w, h, my_background):
    my_canvas = world.ca(width=w, height=h, background=my_background)
    return my_canvas

def create_rectangle(width,hieght,color):
    rec = rectangle()
    rec.width = width
    rec.height = hieght
    rec.color = color
    rec.corner = point()
    rec.corner.x = 0
    rec.corner.y = 0
    return rec
    
canvas = create_canvas(world,500,500,'white')

rec = create_rectangle(100,100,'red')

print draw_rectangle(canvas,rec)


world.mainloop()
