def getDelta(start_cords, r, u):
    """
    :param a: нормальное ускорение
    :param start_cords: начальное положения тела в пространстве
    :param r: радиус окружности по которой движется тело
    :return: выдаёт координаты движения
    """
    from math import sin, cos, pi

    return start_cords[0] + r * sin(pi * u/180), start_cords[1] + r * cos(pi * u/180)


def getOvalCoords(x,y,r):
    return x + r, y + r, x - r, y - r


if __name__ == "__main__":
    print('Файл model был запущен')


else:
    print("Файл model был заимпортирован")