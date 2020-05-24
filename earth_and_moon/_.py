from tkinter import *
from math import sin, cos, pi
import random

root = Tk()

# root.resizable(width=False, height=False)

c = Canvas(root, width=1000, height=1000, bg='#fff')
c.pack()


def esc(event):
    root.destroy()


root.bind('<Escape>', esc)

r1 = 15
r2 = 100
x0, y0 = 250,250
u = 0


oval = c.create_oval(x0 + r2, y0 + r2, x0 - r2, y0 - r2)
x = x0 + r1 * sin(pi * u / 180)
y = y0 - r1 * cos(pi * u / 180)
circle = c.create_oval(x + r2 + r1, y + r1, x - r1 + r2, y - r1)



def drawEarth ():
    global c
    global x
    global y
    global u
    u = u + 1
    x = x0 + r2 * sin(pi * u / 180)
    y = y0 - r2 * cos(pi * u / 180)
    c.moveto(circle, x,y)
    root.after(5, drawEarth)

def main():
    drawEarth()
    root.mainloop()


main()