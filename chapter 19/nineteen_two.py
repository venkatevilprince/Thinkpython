from swampy.Gui import *
g = Gui()
g.title("Gui")
canvas = g.ca(width=500, height=500)
canvas.config(bg='grey')


def draw_circle():
    canvas.polygon([[0, 100], [100, 200], [200, 100]],fill='blue', outline='orange', width=5)
    canvas.line([[0, 100], [100, 200], [200, 100], [0, 100]], width=1)
    canvas.circle([0, 0], 100, fill='red')
g.bu(text='create figures', command=draw_circle)
g.mainloop()
