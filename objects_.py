from model import getCoordY


def speedX(Object, weight: float, distance: float) -> float:
    """
    :param Object: объект
    :param weight: масса вокруг вращающегося по орбите тела
    :param distance: расстояние до вращающегося тела в данный момент
    :return: скорость объекта по оси X
    """
    G = 6.67 * 10e-11
    F = G * Object.weight * weight / (distance ** 2)
    a = F / weight
    v = (a * distance) ** 0.5 / 70000000
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
        """
        self.x = -R1
        self.y = 0
        self.R1 = R1
        self.R2 = R2
        self.v = v
        self.direction = 1
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
        return [self.x, self.y]

    def updateSpeed(self, speed):
        """
        updateSpeed(speed) изменяем текущую скорость по оси OX на speed
        :param speed: новая скорость
        """
        self.v = speed

    def getDistanceFromPlanet (self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Planet:
    """
    :param name: Название планеты
    :param m:  массы планеты в кг
    :param radius: радиус планеты
    :param R1: радиус1 эллипса вокруг которого движется планета
    :param R2: радиус2 эллипса вокруг которого движется планета
    :param satellites: её спутники, объекты типа satellite
    :param coords: координаты планеты
    """

    def __init__(self, name: str, weight: float, radius: float, R1, R2, *satellites: list, color="black", scale=200000):
        """
        :param name: Название планеты
        :param m:  массы планеты в кг
        :param radius: радиус планеты
        :param R1: радиус1 эллипса вокруг которого движется планета
        :param R2: радиус2 эллипса вокруг которого движется планета
        :param satellites: её спутники, объекты типа satellite
        :param coords: координаты планеты
        """

        self.name = name
        self.weight = weight
        self.radius = radius / scale
        self.start_coords = []
        self.satellites = list(satellites)
        self.R1 = R1 / scale
        self.R2 = R2 / scale
        self.coords = None
        self.oval = None
        self.distance = R1
        self.star_weight = None
        self.speed = None

    def initStartParams(self, start_coords, radius, weight):
        """
        Инициализация начальных параметров Спутника
        """
        self.R1 += radius
        self.R2 += radius
        self.star_weight = weight
        self.start_coords = start_coords
        self.speed = speedX(self, weight, self.distance)
        self.coords = Coords(self.R1, self.R2, self.speed, self.start_coords)
        self.initStartSattelCoords()

    def initStartSattelCoords(self):
        """
        Инициализируем положения спутников нашей планеты
        """

        for st in self.satellites:
            st.initStartParams(self.start_coords, self.radius, self.weight, self.star_weight, self.R1, self.R2, self.coords)

    def getDeltaCoords(self):
        coords = self.coords.getNextCoords()
        return coords

    def getCoords(self) -> list:
        """
        :return: Возвращает положение планеты в данный момент
        """
        coords = self.getDeltaCoords()
        return list(map(lambda a, b: a + b, self.start_coords, coords))

class Satellite:
    """
    :param name: название спутника
    :param m: масса спутника, в кг
    :param radius: радиус спутника
    :param R: расстояние до планеты-сородича
    :param R1: радиус1 движения по эллипсу
    :param R2: радиус2 движения по эллипсу
    """

    def __init__(self, name: str, weight: object, radius: object, R1: object, R2: object, color: object = "gray", scale=200000) -> object:
        """
        :param name: название спутника
        :param m: масса спутника, в кг
        :param radius: радиус спутника
        :param R: расстояние до планеты-сородича
        :param R1: радиус1 движения по эллипсу
        :param R2: радиус2 движения по эллипсу
        """

        self.name = name
        self.weight = weight
        self.radius = radius / scale
        self.R1 = R1 / scale
        self.R2 = R2 / scale
        self.earthDistance = R1
        self.starDistance = None
        self.start_coords = []
        self.oval = None
        self.planetSpeed = None
        self.starSpeed = None
        self.planetDeltaCoords = None
        self.starDeltaCoords = None

    def initStartParams(self, coords: list, r: float, planetWeight: float, starWeight: float, R1, R2, PlanetCoords):
        """
        :param coords: координаты планеты, понадобятся для вычислений
        :param r: радиус планеты, понадобятся для вычислений
        :param planetWeight: масса планеты, понадобятся для вычислений
        :param starWeight: масса планеты, понадобятся для вычислений
        :param R1: радиус планеты относительно звезды
        :param R2: радиус планеты относительно звезды
        """
        self.R1 += r
        self.R2 += r
        self.start_coords = coords[0], coords[1]
        self.planetSpeed = speedX(self, planetWeight, self.earthDistance) * 400
        self.planetDeltaCoords = Coords(self.R1, self.R2, self.planetSpeed, self.start_coords)
        self.starDeltaCoords = PlanetCoords

    def getCoords(self) -> list():
        """;
        :return: массив значений где первый элемент новая координата по оси OX, второй элемент новая координата по оси OY
        """
        # self.distance = self.planetDeltaCoords.getDistanceFromPlanet()
        # self.v = speedX(self, self.weight, self.distance)
        # self.planetDeltaCoords.updateSpeed(self.v)
        deltaCoords1 = self.planetDeltaCoords.getNextCoords()
        deltaCoords2 = self.starDeltaCoords.getNextCoords()

        return list(map(lambda a, b, c: a + b + c, self.start_coords, deltaCoords1, deltaCoords2))


class Star:
    """
    :param name: название звезды
    :param weight: масса звезды
    :param radius: радиус звезды
    :param start_coords: начальное положения звезды в области Tkinter
    :param planets: планеты которые вращаются вокруг звезды
    """

    def __init__(self, name: str, weight: float, radius: float, start_coords: list(), *planets, color="yellow", scale=200000):
        """
        :param name: название звезды
        :param weight: масса звезды
        :param radius: радиус звезды
        :param start_coords: начальное положения звезды в области Tkinter
        :param planets: планеты которые вращаются вокруг звезды
        """

        self.name = name
        self.weight = weight
        self.radius = radius / scale
        self.start_coords = start_coords
        self.planets = planets
        self.color = color
        self.initStartPlanetParams()

    def initStartPlanetParams(self):
        for planet in self.planets:
            planet.initStartParams(self.start_coords, self.radius, self.weight)



if __name__ == "__main__":
    print('Файл Objects был запущен')
    pl = Planet()
else:
    print("Файл Objects был заимпортирован")
