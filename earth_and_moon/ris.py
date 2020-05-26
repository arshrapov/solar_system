from tkinter import *
from model import getOvalCoords


def draw(planets, w, h, ts):
    """
    :param planets: список планет, которые являются объектами типа  Planet
    :param w: целое число, используются для обозначения ширины окна
    :param h: целое число, используются для обозначения высоты окна
    :param ts: время, в мс, частота кадров
    :return:
    """
    root = Tk()
    cnv = Canvas(root, width=w, height=h, bg='white')
    cnv.pack()

    def drawStartPosition():
        """
        Рисуем первое состояние нашей системы
        """
        for planet in planets:
            coords = getOvalCoords(planet.coords[0], planet.coords[1], planet.radius)
            cnv.create_oval(coords[0], coords[1], coords[2], coords[3])
            for satellite in planet.satellites:
                st_coords = satellite.getCoords()
                st_oval_coords = getOvalCoords(st_coords[0], st_coords[1], satellite.radius)
                satellite.oval = cnv.create_oval(st_oval_coords[0], st_oval_coords[1], st_oval_coords[2],
                                                 st_oval_coords[3])

    def movement():
        """
        Последовательно рисуем каждое последующее состояние нашей системы, где задержка между кадрами - ts
        """
        for planet in planets:
            for satellite in planet.satellites:
                st_coords = satellite.getCoords()
                cnv.moveto(satellite.oval, st_coords[0], st_coords[1])

        root.after(ts, movement)

    drawStartPosition()
    movement()
    root.mainloop()


if __name__ == "__main__":
    print('Файл ris был запущен')
else:
    print("Файл ris был заимпортирован")
