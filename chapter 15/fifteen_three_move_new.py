import copy
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
rec = rectangle()
rec.width = 100
rec.height = 50
rec.corner = point()
rec.corner.x = 0
rec.corner.y = 0
print "Before moving rectangle ",
print_coordinates_rec(rec)
new_rec = move_rectangle(rec,10,5)
print "After moving rectangle ",
print_coordinates_rec(rec)
print "Newly created rectangle ",
print_coordinates_rec(new_rec)
