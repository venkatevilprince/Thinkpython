class point(object):
    """represents x and y coordinates"""
class rectangle(object):
    """Represents a rectangle

    attributes: width, height, corner"""


def print_coordinates_rec(rec):
    print "({}, {})".format(rec.corner.x,rec.corner.y)


def move_rectangle(rect,dx,dy):
    """move the rectange bu shifting the coordinates by dx and dy"""
    rect.corner.x += dx
    rect.corner.y += dy

rec = rectangle()
rec.width = 100
rec.height = 50
rec.corner = point()
rec.corner.x = 0
rec.corner.y = 0
print_coordinates_rec(rec)
move_rectangle(rec,10,5)
print_coordinates_rec(rec)





