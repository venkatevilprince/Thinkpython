from swampy.Gui import *
from Tkinter import PhotoImage

g = Gui()
photo = PhotoImage(file='danger.gif')
g.bu(image=photo)

canvas = g.ca(width=300)
canvas.image([500,0], image=photo)

import Image as PIL
import ImageTk

image = PIL.open('1.jpg')
photo = ImageTk.PhotoImage(image)
g.la(image=photo)

g.mainloop()
