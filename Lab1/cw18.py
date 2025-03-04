from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self) -> int:
        pass 


class Car(Vehicle):

    def __init__(self, maximum_speed: int) -> None:
        self.maximum_speed = maximum_speed        

    def max_speed(self, value: int) -> None:
        self.maximum_speed = value

class Bicycle(Vehicle):

    def __init__(self, maximum_speed: int) -> None:
        self.maximum_speed = maximum_speed        

    def max_speed(self, value: int) -> None:
        self.maximum_speed = value


def main():
    car = Car(300)
    print(car.maximum_speed)
    car.max_speed(500)
    print(car.maximum_speed)

    bicycle = Bicycle(30)
    print(bicycle.maximum_speed)
    bicycle.max_speed(50)
    print(bicycle.maximum_speed)


if __name__ == '__main__':
    main()

