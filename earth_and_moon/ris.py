from tkinter import *
from model import getOvalCoords



def draw(planets):
    root = Tk()
    c = Canvas(root, width=1000, height=1000, bg='white')
    c.pack()


    def dr():
        for planet in planets:
            coords = getOvalCoords(planet.coords[0], planet.coords[1], planet.r)
            c.create_oval(coords[0], coords[1], coords[2], coords[3])
            for st in planet.satellites:
                st_coords = st.getCoords()
                st_oval_coords = getOvalCoords(st_coords[0], st_coords[1], st.r)

                st.oval = c.create_oval(st_oval_coords[0], st_oval_coords[1], st_oval_coords[2], st_oval_coords[3])


    def movement():
        for planet in planets:
            for st in planet.satellites:
                st_coords = st.getCoords()
                c.moveto(st.oval, st_coords[0], st_coords[1])
        root.after(10, movement)


    dr()
    root.mainloop()


if __name__ == "__main__":
    print('Файл ris был запущен')
else:
    print("Файл ris был заимпортирован")