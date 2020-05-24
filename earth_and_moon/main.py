def main():
    import ris
    import objects_ as objc

    planets = [objc.Planet("Земля",
                           5.97e24, 30000, [400, 400], objc.satellite("Луна", 7.35e22, 5000, 70000)) ]
    ris.draw(planets)


if __name__ == "__main__":
    main()
