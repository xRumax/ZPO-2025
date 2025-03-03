from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    pi = 3.14
    r: float
    def __init__(self, r: float)-> None:
        self.r = r

    def area(self) -> float:
        return self.pi * (self.r*self.r)

class Rectangle(Shape):
    sideA: float
    sideB: float
    def __init__(self, sideA:float, sideB:float) -> None:
        self.sideA = sideA
        self.sideB = sideB

    def area(self) -> float:
        return self.sideA * self.sideB

def main():
    rect = Rectangle(4,5)
    circle = Circle(3)
    print(rect.area())
    print(circle.area())



if __name__ == '__main__':
    main()