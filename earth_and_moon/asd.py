from tkinter import *
from math import sin, cos
import random

root = Tk()


c = Canvas(root, width=1980, height=1000, bg='#000000')
c.pack()


def esc (event):
    root.destroy()


root.bind('<Escape>', esc)

EarthPhoto = PhotoImage(file='globe.png')
Earth = c.create_image(50, 10, image=EarthPhoto, anchor=NW)
x = 0
y = 0


def drawEarth ():
    global c
    global x
    global y

    c.move(Earth, sin(-5), cos(5))
    coordinates = c.coords(Earth)

    x = coordinates[0]
    y = coordinates[1]

    root.after(15, drawEarth)


def main ():
    drawEarth()
    root.mainloop()


main()