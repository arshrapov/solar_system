from model import getCoordY


def speedX(Satellite, weight: float, distance: float) -> float:
    """
    :param Satellite: объект типа спутника
    :param weight: масса планеты, по орбите которой вращается спутник
    :param distance: расстояние до планеты в данный момент
    :return: скорость планеты по оси X
    """
    G = 6.67 * 10e-11
    F = G * Satellite.weight * weight / (distance ** 2)
    a = F / weight
    v = (a * distance) ** 0.5 / 80000000
    return v


class Coords:
    """
    :param R1: Радиус орбиты по OX
    :param R2: Радиус орбиты по OY
    :param v: скорости по оси x
    :param start_cords: положения тела в пространстве Tkinter
    """
    def __init__(self, R1, R2, v, start_cords):
        """
        :param R1: Радиус орбиты по OX
        :param R2: Радиус орбиты по OY
        :param v: скорости по оси x
        :param start_cords: положения тела в пространстве Tkinter
        """
        self.x = -R1
        self.y = 0
        self.R1 = R1
        self.R2 = R2
        self.v = v
        self.direction = 1
        self.start_cords = start_cords
        self.finished = False

    def getNextCoords(self) -> list():
        """
        С учётом перемещения тела выдаёт следующее положения тела в пространстве относительно родителя(планеты или здвезды)
        :return: массив значений, где первый элемент - положения тела по оси OX, а второй элемент - положения тела по оси OY
        """
        if self.x >= self.R1:
            self.direction = -1
            self.finished = 1
        if self.x <= -self.R1 and self.finished:
            self.direction = 1
            self.finished = 0

        self.y = self.direction * getCoordY(self.x, self.R1, self.R2)
        self.x += self.direction * self.v
        return list(map(lambda a, b: a + b, [self.x, self.y], self.start_cords))

    def updateSpeed(self, speed):
        """
         updateSpeed(speed) изменяем текущую скорость по оси OX на speed
        :param speed: новая скорость
        """
        self.v = speed

    def getDistanceFromPlanet (self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class Planet:

    def __init__(self, name: str, weight: float, radius: float, coords: list(), *satellites: list, color="black"):
        """
        :param name: Название планеты
        :param m:  массы планеты в кг
        :param radius: радиус планеты
        :param satellites: её спутники, объекты типа satellite
        :param coords: координаты планеты
        """
        self.name = name
        self.weight = weight
        self.radius = (radius / 500)
        self.coords = coords
        self.satellites = list(satellites)
        self.initStartSattelCoords()

    def initStartSattelCoords(self):
        """
        Инициализируем положения спутников нашей планеты
        """
        for st in self.satellites:
            st.initStartParams(self.coords, self.radius, self.weight)


class Satellite:

    def __init__(self,name, weight, radius, R1, R2, color="gray"):
        """
        :param name: название спутника
        :param m: масса спутника, в кг
        :param radius: радиус спутника
        :param R: расстояние до планеты-сородича
        """

        self.name = name
        self.weight = weight
        self.radius = radius / 500
        self.R1 = R1 / 500
        self.R2 = R2 / 500
        self.distance = R1
        self.start_coords = []
        self.oval = None
        self.v = None
        self.coords = None

    def initStartParams(self, coords, r, M):
        """
        :param coords: координаты планеты, понадобятся для вычислений
        :param r: радиус планеты, понадобятся для вычислений
        :param M: масса планеты, понадобятся для вычислений
        """
        self.R1 += r
        self.R2 += r
        self.start_coords = [coords[0], coords[1]]
        self.v = speedX(self, M, self.distance)
        self.coords = Coords(self.R1, self.R2, self.v, self.start_coords)

    def getCoords(self) -> list:
        """
        :return: массив значений где первый элемент новая координата по оси OX, второй элемент новая координата по оси OY
        """
        self.distance = self.coords.getDistanceFromPlanet()
        self.v = speedX(self, self.weight, self.distance)
        self.coords.updateSpeed(self.v)
        return self.coords.getNextCoords()


if __name__ == "__main__":
    print('Файл Objects был запущен')

else:
    print("Файл Objects был заимпортирован")
