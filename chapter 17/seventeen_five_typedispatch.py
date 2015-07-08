class point(object):
    """x and y coordinates"""


    def __init__(self,x=0,y=0):
        """initialises values of x and y with the parameters"""
        self.x = x
        self.y = y


    def __str__(self):
        """returns the value of x and y and prints with print statement"""
        return "({}, {})".format(self.x,self.y)


    def __add__(self,other):
        p = point()
        if isinstance(other, point):
            p.x = self.x + other.x
            p.y = self.y + other.y
        elif isinstance(other, tuple):
            p.x = self.x + other[0]
            p.y = self.x + other[1]
        else:
            print"wrong type"
            raise TypeError('Wrong type')
        return p


    def __radd__(self, other):
       return self.__add__(other)
p1 = point(10,2)
p2 = point(10,2)
print p1 + p2
print p1 + (10,20)
print (10,30) + p1   #test for __radd__
