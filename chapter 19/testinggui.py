from swampy.Gui import *


class Vector(Gui):
    def __init__(self):
        self.canvas = self.ca(width=500, height=500, bg='white')
        #self.tag = 0
        self.bind('<ButtonPress-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.drop)
    

g = Gui()
#ca = g.ca(width=500, height=500, bg='white')

vec = Vector()


item = ca.rectangle([[-250,-250],[100,100]], fill='red')
print type(item)
g.mainloop()
