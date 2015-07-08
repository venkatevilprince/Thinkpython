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
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
        
p1 = point(10,2)
p2 = point(10,2)
print p1+p2
