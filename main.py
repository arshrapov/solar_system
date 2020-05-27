def main():
    import ris
    import objects_ as objc

    stars = {objc.Star("Звезда", 8.87e45, 150000, [740, 340], objc.Planet("Планета", 5.97e25, 25000, 300000, 500000,
                           objc.Satellite("Спутник1", 7.35e22, 5000, 100000, 75000),
                           objc.Satellite("Спутник2", 7.35e21, 3500, 100000, 99000)))}

    ris.draw(stars, 1980, 1000, 1)


if __name__ == "__main__":
    main()

