def getDelta(start_cords, v, u):
    """
    :param a: нормальное ускорение
    :param start_cords: начальное положения тела в пространстве
    :param v: линейная скорость тела
    :return: выдаёт координаты движения
    """
    from math import sin, cos, pi

    return start_cords[0] + v * sin(pi * u / 90), start_cords[1] + v * cos(pi * u / 90)


def getOvalCoords(x, y, r):
    return x + r, y + r, x - r, y - r


if __name__ == "__main__":
    print('Файл model был запущен')


else:
    print("Файл model был заимпортирован")