class point(object):
    """x and y coordinates"""


    def __init__(self,x=0,y=0):
        """initialises values of x and y with the parameters"""
        self.x = x
        self.y = y


    def __str__(self):
        """returns the value of x and y and prints with print statement"""
        return "({}, {})".format(self.x,self.y)
p = point(10,2)
print p
