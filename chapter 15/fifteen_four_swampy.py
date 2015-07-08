import copy
import sys
import os
from swampy.World import *


class point(object):
    """represents x and y coordinates"""


class rectangle(object):
    """Represents a rectangle

    attributes: width, height, corner, color"""


def print_coordinates_rec(rec):
    print "({}, {})".format(rec.corner.x, rec.corner.y)


def move_rectangle(rect, dx, dy):
    """move the rectange bu shifting the coordinates by dx and dy"""
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect


class polygon:
    """Represents a polygon

       attributes: list of corners point objects"""


class circle(object):
    """Represents a circle

    attributes: radius ,corner ,color"""
world = World()


def create_bbox_rect(rect):
    p1 = []
    p1.append(rect.corner.x)
    p1.append(rect.corner.y)
    p2 = []
    p2.append(rect.corner.x + rect.width)
    p2.append(rect.corner.y + rect.height)
    box = []
    box.append(p1)
    box.append(p2)
    return box


def draw_rectangle(canvas, rect):
    bbox = create_bbox_rect(rect)
    canvas.rectangle(bbox, outline='black', width=2, fill='red')


def create_canvas(world, w, h, my_background):
    my_canvas = world.ca(width=w, height=h, background=my_background)
    return my_canvas


def create_rectangle(width, hieght, color, x, y):
    rec = rectangle()
    rec.width = width
    rec.height = hieght
    rec.color = color
    rec.corner = point()
    rec.corner.x = x
    rec.corner.y = y
    return rec


def create_circle(radius, color, x, y):
    cir = circle()
    cir.r = radius
    cir.color = color
    cir.corner = point()
    cir.corner.x = x
    cir.corner.y = y
    return cir


def create_polygon(*points):
    poly = polygon()
    all_list = []
    for i in range(len(points)-1):
        plist = [points[i].x, points[i].y]
        all_list.append(plist)
    poly.points = all_list
    poly.color = points[len(points)-1]
    return poly


def create_point(x, y):
    p = point()
    p.x = x
    p.y = y
    return p


def draw_point(canvas, point):
    draw_point_rect = create_rectangle(3, 3, 'black', 0, 0)
    draw_point_rect.corner.x = point.x
    draw_point_rect.corner.y = point.y
    print draw_point_rect.corner.y
    draw_rectangle(canvas, draw_point_rect)


def draw_circle(canvas, circle):
    bbox = (circle.corner.x, circle.corner.y)
    canvas.circle(bbox,  circle.r, outline=None, fill=circle.color)


def draw_polygon(canvas, poly):
    canvas.polygon(poly.points, fill=poly.color)
canvas = create_canvas(world, 500, 500, 'grey')
point1 = point()
point1.x = 100
point1.y = 50
rec = create_rectangle(100, 50, 'red', 0, 0)
"""uncomment the draw functions to see the circles and rectangles"""
#draw_rectangle(canvas,rec)
#draw_point(canvas, point1)
circ = create_circle(100, 'green', -100, -50)
#draw_circle(canvas, circ)
"""This program draws the Czech republic's Flag using the swampy library"""
p1 = create_point(-200, 100)
p2 = create_point(-200, -100)
p3 = create_point(0, 0)
poly1 = create_polygon(p1, p2, p3, 'RoyalBlue4')
draw_polygon(canvas, poly1)
p1 = create_point(-200, 100)
p2 = create_point(0, 0)
p3 = create_point(200, 0)
p4 = create_point(200, 100)
poly2 = create_polygon(p1, p2, p3, p4, 'white')
draw_polygon(canvas, poly2)
p1 = create_point(-200, -100)
p2 = create_point(0, 0)
p3 = create_point(200, 0)
p4 = create_point(200, -100)
poly2 = create_polygon(p1, p2, p3, p4, 'red2')
draw_polygon(canvas, poly2)
world.mainloop()
