from tkinter import *
from math import sin, cos

root = Tk()


c = Canvas(root, width=1980, height=1000, bg='#fff')
c.pack()


def func(x, r, vec):
    y = vec * ((r * r - x * x) ** 0.5)
    if type(y) == type(1j):
        return -0.2
    return y


r = 10
R = 200
0
start_coords =[330, 330]
x = []
y = []


def nextCoord(x, R, vec):
    y = vec * (round((R * R - x * x) ** 0.5, 5))
    if type(y) == type(1j):
        return 0
    return y

c.create_line(start_coords[0] - 200, start_coords[1], start_coords[0] + 200, start_coords[1])
c.create_line(start_coords[0], start_coords[1] - 200 , start_coords[0], start_coords[1] + 200)
center = c.create_oval(start_coords[0] + 5 * r, start_coords[1] + 5 * r, start_coords[0] - 5 * r, start_coords[1] - 5 * r, fill="yellow")
start_coords = [start_coords[0], start_coords[1]]
circle = c.create_oval(start_coords[0] + r, start_coords[1] + r, start_coords[0] - r, start_coords[1] - r, fill="green")

vec = 1
finished = 0
start_coords[0] -= r
start_coords[1] -= r
x = - R
y = 0

print(x, y)


def main():
    global vec
    global x,y
    global finished
    print(x, y
          )
    # if x == -R:
    #     c.create_rectangle(start_coords[0] - r + x, start_coords[1] - r + y, start_coords[0] + r + x, start_coords[1] + r + y)
    # if x == R:
    #     c.create_rectangle(start_coords[0] - r + x, start_coords[1] - r + y, start_coords[0] + r + x,
    #                         start_coords[1] + r + y)
    if x >= R:
        vec = -1
        finished = 1
        print("y")
    if finished == 1 and x <= -R:
        vec = 1

        finished = 0
    y = func(x, R, vec)
    print(x, y)
    c.moveto(circle, x + start_coords[0], y + start_coords[1])
    x += vec * 0.1
    root.after(5, main)


main()
root.mainloop()