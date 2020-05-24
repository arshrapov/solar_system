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
        self.normalAcceleration()

    def normalAcceleration(self):
        for st in self.satellites:
            st.acceleration = 0.3
            print(st.R)
            st.coords = [self.coords[0] - st.R, self.coords[1]]
            print(st.coords, self.coords)
            st.deltaCoords()


class satellite:

    def __init__(self,name, m, r, R):
        """
        :param name: название спутника
        :param m: масса спутника, в кг
        :param r: радиус спутника
        :param R: расстояние до планеты-сородича
        """
        self.name = name
        self.m = m
        self.r = r / 1000
        self.R = R / 1000
        self.acceleration = None
        self.coords = []
        self.u = 0
        self.w = 0
        self.oval = None

    def getCoords(self):
        from model import getDelta
        self.coords =  getDelta(self.coords, self.R, self.u)
        self.u += self.acceleration
        return self.coords

    def deltaCoords(self):
        self.coords = [self.coords[0], self.coords[1]]


if __name__ == "__main__":
    print('Файл Objects был запущен')

else:
    print("Файл Objects был заимпортирован")