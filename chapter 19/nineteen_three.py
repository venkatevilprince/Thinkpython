from swampy.Gui import *
g = Gui()
g.title("Gui")


text = g.te(width=100, height=5)
canvas = g.ca(width=300, height=300)
canvas.config(bg='grey')
circle = None
def change_color():
    global circle
    color = entry.get()
    print color
    if circle == None:
        return
    circle.config(fill=color)

def draw_circle():
    global circle
    circle = canvas.circle([0, 0], 100, fill='red')

g.bu(text='create circle', command=draw_circle)
entry = g.en()
g.bu(text='change color', command=change_color)



g.mainloop()
