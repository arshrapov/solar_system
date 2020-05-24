def acceleration(satellite, m):
    """
    :param satellite: объект типа спутника
    :param m: масса планеты, по орбите которой вращается спутник
    :return: центростриметельное ускорение по орбите планеты
    """
    pass


class Planet:

    def __init__(self, name, m, r, coords, *satellites):
        """
        :param name: Название планеты
        :param m:  массы планеты в кг
        :param r: радиус планеты
        :param satellites: её спутники, объекты типа satellite
        :param coords: координаты планеты
        """
        self.name = name
        self.m = m
        self.r = (r / 1000)
        self.coords = coords
        self.satellites = list(satellites)
        self.initStCoords(self.coords)

    def initStCoords(self, coords):
        for st in self.satellites:
            st.initStartCoords(coords, self.r)



class satellite:

    def __init__(self,name, m, r, R, T):
        """
        :param name: название спутника
        :param m: масса спутника, в кг
        :param r: радиус спутника
        :param R: расстояние до планеты-сородича
        :param T: период обращения вокруг планеты, в земных днях
        """

        from math import pi

        self.name = name
        self.m = m
        self.r = r / 1000
        self.R = R / 1000
        self.T = T
        self.acceleration = T / 360
        self.coords = []
        self.u = 0
        self.w = 0
        self.v = 2 * pi * self.R / 180
        self.oval = None

    def initStartCoords(self, coords, r):
        self.coords = [coords[0] - self.R - self.r /2, coords[1] - self.r /2]
        self.R += r
    def getCoords(self):
        from model import getDelta
        self.coords = getDelta(self.coords, self.v, self.u)
        self.u += self.acceleration
        return self.coords


if __name__ == "__main__":
    print('Файл Objects был запущен')

else:
    print("Файл Objects был заимпортирован")