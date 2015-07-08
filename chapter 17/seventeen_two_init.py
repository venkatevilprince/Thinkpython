class point(object):
    """x and y coordinates"""


    def __init__(self,x=0,y=0):
        """initialises values of x and y with the parameters"""
        self.x = x
        self.y = y


    def print_point(self):
        """prints the value of x and y"""
        print "({}, {})".format(self.x,self.y)
p = point(10,2)
p.print_point()
