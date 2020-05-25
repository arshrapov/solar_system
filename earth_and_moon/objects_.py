def speedX(satellite, m, R):
    """
    :param satellite: объект типа спутника
    :param m: масса планеты, по орбите которой вращается спутник
    :return: скорость планеты по оси X
    """
    G = 6.67 * 10e-11
    F = G * satellite.m * m / (R ** 2)
    a = F / m
    return (a * R) ** 0.5 / 1000000


class Coords:
    """
    :param R: Радиус орбиты
    :param v: скорости по оси x
    :param start_cords: положения тела в пространстве Tkinter
    """
    def __init__(self, R, v, start_cords):
        """
        :param R: Радиус орбиты
        :param v: скорости по оси x
        :param start_cords: положения тела в пространстве Tkinter
        """
        self.x = -R
        self.y = 0
        self.R = R
        self.v = v
        self.direction = 1
        self.start_cords = start_cords
        self.finshed = False

    def getNextCoords(self):
        from model import func

        if self.x >= self.R:
            self.direction = -1
            self.finshed = 1
        if self.x <= -self.R and self.finshed:
            self.direction = 1
            self.finshed = 0

        print(self.direction * func(self.x, self.R))
        print(self.y, "==", end ='')
        self.y = self.direction * func(self.x, self.R)
        print(self.y)
        coords = [self.x, self.y]
        self.x += self.direction * self.v
        return list(map(lambda a, b: a + b, [self.x, self.y], self.start_cords))


class Planet:

    def __init__(self, name, m, r, coords, *satellites, color="black"):
        """
        :param name: Название планеты
        :param m:  массы планеты в кг
        :param r: радиус планеты
        :param satellites: её спутники, объекты типа satellite
        :param coords: координаты планеты
        """
        self.name = name
        self.m = m
        self.r = (r / 500)
        self.coords = coords
        self.satellites = list(satellites)
        self.initStCoords(self.coords)

    def initStCoords(self, coords):
        for st in self.satellites:
            st.initStartParams(coords, self.r, self.m)


class satellite:

    def __init__(self,name, m, r, R, color="gray"):
        """
        :param name: название спутника
        :param m: масса спутника, в кг
        :param r: радиус спутника
        :param R: расстояние до планеты-сородича
        """

        from math import pi

        self.name = name
        self.m = m
        self.r = r / 500
        self.R = R / 500
        self.start_coords = []
        self.oval = None
        self.v = None
        self.coords = None

    def initStartParams(self, coords, r, M):
        self.start_coords = [coords[0], coords[1]]
        self.v = speedX(self, M, self.R)
        self.coords = Coords(self.R, self.v, self.start_coords)

    def getCoords(self):
        return self.coords.getNextCoords()


if __name__ == "__main__":
    print('Файл Objects был запущен')

else:
    print("Файл Objects был заимпортирован")
