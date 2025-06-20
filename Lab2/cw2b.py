from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal() -> Animal:
        pass
        
class Dog(Animal):
    def make_sound(self) -> None:
        print('Woof')

class Cat(Animal):
    def make_sound(self) -> None:
        print('Meow')

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()
    
class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()
    
class Factory:
    _factories: dict
    def __init__(self) -> None:
        self._factories = {
            "dog": DogFactory,
            "cat": CatFactory,
        }
    
    def create_animal(self, type_:str) -> Animal:
        return self._factories[type_]().create_animal()
    

def main():
    factory = Factory()
    dog = factory.create_animal('dog')
    cat = factory.create_animal('cat')

    dog.make_sound()
    cat.make_sound()

if __name__ == "__main__":
    main()