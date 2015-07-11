from swampy.Gui import *


class Vector(Item):

    def __init__(self, item):
        self.canvas = item.canvas
        self.tag = item.tag
        self.bind('<ButtonPress-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.drop)

    #def rectangling(self,event):

    def select(self, event):
        """Selects this item for dragging."""
        print "select occurs"
        self.dragx = event.x
        self.dragy = event.y

        self.fill = self.cget('fill')
        #self.config(fill='orange')
        
        
    
    def drag(self, event):
        """Move this item using the pixel coordinates in the event object."""
        # see how far we have moved
        #dx = event.x - self.dragx
        #dy = event.y - self.dragy

        pos = ca.canvas_coords([[self.dragx, self.dragy],[event.x,event.y]])
        print pos
        item = ca.rectangle(pos, fill='red')
        # move the item 
        #self.move(dx, dy)

    def drop(self, event):
        """Drops this item."""
        self.config(fill=self.fill)
    

g = Gui()
ca = g.ca(width=500, height=500, bg='white')

item = ca.rectangle([[-250,-250],[100,100]], fill='red')

vec = Vector(item)
ca.bind('<ButtonPress-1>', vec.select)

def make_circle(event):
        """Makes a circle item at the location of a button press."""
        dx = event.x 
        dy = event.y 
        pos = ca.canvas_coords([[event.x, event.y],[event.x+10, event.y+10] ])
        print pos
        item = ca.rectangle(pos, fill='red')
        item = Vector(item)

ca.bind('<ButtonPress-3>', make_circle)

def make_text(event=None):
    """Pressing Return in the Entry makes a text item."""
    text = en.get()
    item = ca.text([0,0], text)
    item = Vector(item)

g.row([0,1])
bu = g.bu('Make text item:', make_text)
en = g.en()
en.bind('<Return>', make_text)
        
g.mainloop()
