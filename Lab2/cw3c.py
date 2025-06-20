from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

@dataclass 
class Screen:
    diagonal: float
    type_of_glass: str = field(default = 'shiny')

@dataclass 
class Battery:
    capacity: int

@dataclass
class Body:
    color: str
    size: tuple =field(default = (6, 3))

@dataclass
class Camera:
    Mpx: int
    amount: int = field(default = 3)

class Factory(ABC):
    @abstractmethod
    def produce_screen(self, diagonal: float) -> float:
        pass

    @abstractmethod
    def produce_battery(self, capacity:int) -> int:
        pass

    @abstractmethod
    def produce_body(self, color:str) -> Body:
        pass

    @abstractmethod
    def produce_camera(self, Mpx:int) -> int:
        pass

class ApfelFactory(Factory):
    def produce_screen(self, diagonal: float) -> Screen:
        return Screen(diagonal = diagonal)

    def produce_battery(self, capacity: int) -> Battery:
        return Battery(capacity= capacity)
    
    def produce_body(self, color: str) -> Body:
        return Body(color=color)
    
    def produce_camera(self, Mpx: int) -> Camera:
        return Camera(Mpx=Mpx)

class SzajsungFactory(Factory):
    def produce_screen(self, diagonal: float) -> Screen:
        return Screen(diagonal = diagonal, type_of_glass="matte")

    def produce_battery(self, capacity: int) -> Battery:
        return Battery(capacity= capacity)
    
    def produce_body(self, color: str) -> Body:
        return Body(color=color)
    
    def produce_camera(self, Mpx: int) -> Camera:
        return Camera(Mpx=Mpx, amount= 4)

class MajfonFactory(Factory):
    def produce_screen(self, diagonal: float) -> Screen:
        return Screen(diagonal = diagonal, type_of_glass="gorilla")

    def produce_battery(self, capacity: int) -> Battery:
        return Battery(capacity= capacity)
    
    def produce_body(self, color: str) -> Body:
        return Body(color=color, size=(7, 4))
    
    def produce_camera(self, Mpx: int) -> Camera:
        return Camera(Mpx=Mpx, amount= 4)

class AbstractFactory:
    @staticmethod
    def get_factory(model: str)-> Any:
        match model:
            case "Apfel":
                return ApfelFactory()
            case "Szajsung":
                return SzajsungFactory()
            case "Majfon":
                return MajfonFactory()
            case _:
                return ValueError("Product doesn't exist")

def main():
    apfel_factory = AbstractFactory().get_factory("Apfel")

    apfel_screen = apfel_factory.produce_screen(6.5)
    apfel_battery = apfel_factory.produce_battery(4000)
    apfel_body = apfel_factory.produce_body('black')
    apfel_camera = apfel_factory.produce_camera(120)

    print('Apfel specs:')
    print(apfel_screen)
    print(apfel_battery)
    print(apfel_body)
    print(apfel_camera)
    print()

    szajsung_factory = AbstractFactory().get_factory("Szajsung")

    szajsung_screen = szajsung_factory.produce_screen(6.5)
    szajsung_battery = szajsung_factory.produce_battery(4000)
    szajsung_body = szajsung_factory.produce_body('black')
    szajsung_camera = szajsung_factory.produce_camera(120)

    print('Szajsung specs:')
    print(szajsung_screen)
    print(szajsung_battery)
    print(szajsung_body)
    print(szajsung_camera)
    print()


    majfon_factory = AbstractFactory().get_factory("Majfon")

    majfon_screen = majfon_factory.produce_screen(6.5)
    majfon_battery = majfon_factory.produce_battery(4000)
    majfon_body = majfon_factory.produce_body('black')
    majfon_camera = majfon_factory.produce_camera(120)

    print('Majfon specs:')
    print(majfon_screen)
    print(majfon_battery)
    print(majfon_body)
    print(majfon_camera)

if __name__ == "__main__":
    main()

