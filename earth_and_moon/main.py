def main():
    import ris
    import objects_ as objc

    planets = {objc.Planet("Планета", 5.97e22, 30000, [220, 220],
                           objc.Satellite("Спутник1", 7.35e22, 5000, 70000, 50000),
                           objc.Satellite("Спутник2", 7.35e21, 1500, 50000, 30000)),
               objc.Planet("Планета2", 5.87e24, 15000, [400, 400],
                           objc.Satellite("Спутник1", 3.45e22, 5000, 25000, 40000))}

    ris.draw(planets, 660, 660, 1)



if __name__ == "__main__":
    main()
