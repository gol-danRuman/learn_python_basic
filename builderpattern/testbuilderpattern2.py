"Success"
import abc

class Car:
    def __init__(self):
        self.color = None

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def __str__(self):
        return 'Car [color={0}, user={1}]'.format(self.color, self.user)

class CarBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_color(self, color):
        pass

    @abc.abstractmethod
    def set_user(self, user):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass

class CarBuilderImpl(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.set_color(color)

    def set_user(self, user):
        self.car.set_user(user)

    def get_result(self):
        return self.car

class CarBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, color, user):
        self.builder.set_color(color)
        self.builder.set_user(user)
        return self.builder.get_result()


# if __name__ == "__main__":
#     # builder = CarBuilderImpl()
#     # carBuildDirector = CarBuilderDirector(builder)
#     # print(carBuildDirector.construct('blue'))
#     car = CarBuilderDirector(CarBuilderImpl()).construct('Grey', 'Ruman')
#     print(car)
#     print(car.color)
