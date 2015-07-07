import math
class point(object):
    """x and y coordinates"""


def distance_between_points(p1,p2):
    """ Takes 2 objects as parameters and Returns distance between two points"""
    return math.sqrt(abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2)
point1 = point()
point2 = point()
point1.x = 9
point1.y = 7
point2.x = 3
point2.y = 2
print distance_between_points(point1, point2)

    
