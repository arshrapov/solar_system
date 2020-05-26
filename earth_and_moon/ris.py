from tkinter import *
from model import getOvalCoords


def draw(stars, w, h, ts):
    """
    :param planets: список звёзд, которые являются объектами типа Star
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

        for star in stars:
            star_coords = getOvalCoords(star.start_coords[0], star.start_coords[1], star.radius)
            cnv.create_oval(star_coords[0], star_coords[1], star_coords[2], star_coords[3])
            for planet in star.planets:
                planet_oval_coords = list(getOvalCoords(planet.start_coords[0], planet.start_coords[1], planet.radius))
                planet.oval = cnv.create_oval(planet_oval_coords[0], planet_oval_coords[1], planet_oval_coords[2],
                                              planet_oval_coords[3])
                for satellite in planet.satellites:
                    satellite_coords = satellite.getCoords()
                    st_oval_coords = getOvalCoords(satellite_coords[0], satellite_coords[1], satellite.radius)
                    satellite.oval = cnv.create_oval(st_oval_coords[0], st_oval_coords[1], st_oval_coords[2],
                                                     st_oval_coords[3])


    def movement():
        """
        Последовательно рисуем каждое последующее состояние нашей системы, где задержка между кадрами - ts

        """
        # for planet in planets:
        #     for satellite in planet.satellites:
        #         st_coords = satellite.getCoords()
        #         cnv.moveto(satellite.oval, st_coords[0], st_coords[1])
        for star in stars:
            for planet in star.planets:
                planet_coords = planet.getCoords()
                cnv.moveto(planet.oval, planet_coords[0], planet_coords[1])
                for satellite in planet.satellites:
                    satellite_coords = satellite.getCoords()
                    cnv.moveto(satellite.oval, satellite_coords[0], satellite_coords[1])

        root.after(ts, movement)

    drawStartPosition()
    movement()
    root.mainloop()


if __name__ == "__main__":
    print('Файл ris был запущен')
else:
    print("Файл ris был заимпортирован")
