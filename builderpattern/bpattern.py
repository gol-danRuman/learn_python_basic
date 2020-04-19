from builderpattern.testbuilderpattern2 import CarBuilderImpl, CarBuilderDirector

if __name__ == "__main__":
    try:
        car = CarBuilderDirector(CarBuilderImpl()).construct('Grey', 'Ruman')
        print(car)
        print(car.color)
    except Exception:
        print(Exception)

