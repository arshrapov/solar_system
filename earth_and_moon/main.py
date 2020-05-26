def main():
    import ris
    import objects_ as objc

    planets = {objc.Planet("Планета", 5.97e22, 30000, [470, 420],
                           objc.Satellite("Спутник1", 7.35e22, 5000, 100000, 50000),
                           objc.Satellite("Спутник2", 7.35e21, 3500, 75000, 99000)),
               objc.Planet("Планета2", 5.87e24, 15000, [229, 229],
                           objc.Satellite("Спутник1", 3.45e22, 7000, 25000, 90000))}

    ris.draw(planets, 1000, 1000, 1)


if __name__ == "__main__":
    main()
