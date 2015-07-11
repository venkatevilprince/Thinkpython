from swampy.Gui import *
g = Gui()
g.title('Gui')
count = 0
label = g.la(text='Press the button.')


def make_button(n):
        button = g.bu(text='Press me')
        if button:
            make_button(n-1)
        if n == 0:
            return button


def make_label():
    g.la(text='Thank you.')


def print_button():
    global count
    count += 1
    print count,"pressed"
    b = g.bu(text='Press me', command=print_button)
    if(count == 3):
        return
    

def callback1(n):
    print n
    g.bu(text='Now press me.', command=callback2)


def callback2():
    g.la(text='Nice job.')
def a():
    callback1(10)
g.bu(text='Press me.', command=lambda:callback1(10))
g.mainloop()
