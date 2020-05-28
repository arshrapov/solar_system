def main():
    import ris
    import objects_ as objc

    stars = [objc.Star("Солнце", 1.9891e30, 6.9e6, [890, 500],
                       objc.Planet("Меркурий", 3.3e23, 2435, 58e6, 70e6),
                       objc.Planet("Венера", 4.87e24, 6050, 108e6, 130e6),
                       objc.Planet("Земля", 5.97e24, 6377, 149e6, 138e6,
                                   objc.Satellite("", 7.35e22, 1737, 363104, 406696)),
                       objc.Planet("Марс", 6.42e23, 3396, 228e6, 230e6),
                       objc.Planet("", 1.896e28, 69e3, 778e6, 811e6)
                       )]

    ris.draw(stars, 1980, 1000, 1)


if __name__ == "__main__":
    main()

