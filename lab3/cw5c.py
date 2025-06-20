from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_shape(self):
        pass

class Circle(Shape):
    def get_shape(self) -> str:
        return "Circle"
        

class Rectangle(Shape):
    def get_shape(self) -> str:
        return "Rectangle"


class Square(Shape):
    def get_shape(self) -> str:
        return "Square"

class GraphicsTech(ABC):
    shape: Shape

    def __init__(self, shape: Shape) -> None:
        self.shape = shape

    @abstractmethod
    def get_format(self):
        pass

class SVG(GraphicsTech):
    shape: Shape
    def get_format(self)-> str:
        shaper = self.shape.get_shape()
        return f"Format is SVG and shape is {shaper}"

class JPG(GraphicsTech):
    shape: Shape
    def get_format(self)-> str:
        shaper = self.shape.get_shape()
        return f"Format is JPG and shape is {shaper}"



def main():
    shape1 = Circle()
    shape2 = Square()

    graphics_format1 = SVG(shape1)
    graphics_format2 = JPG(shape2)

    print(graphics_format1.get_format())
    print(graphics_format2.get_format())

if __name__ == "__main__":
    main()
