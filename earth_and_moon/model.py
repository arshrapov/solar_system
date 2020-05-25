def func(x, R):
    y = (x*x - R*R) ** 0.5
    if type(y) == type(1j):
        return 0
    return y


def getOvalCoords(x, y, r):
    return x + r, y + r, x - r, y - r


if __name__ == "__main__":
    print('Файл model был запущен')


else:
    print("Файл model был заимпортирован")
