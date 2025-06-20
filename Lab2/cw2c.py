from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

class AnimalFactory:
    _classes = {}

    @classmethod
    def add_animal(cls, animal_type:str, animal_class) -> None:
        cls._classes[animal_type] = animal_class

    @classmethod
    def create_animal(cls, type:str) -> Animal:
        if type not in cls._classes:
            return None
        return cls._classes[type]()
        
class Dog(Animal):
    def make_sound(self) -> None:
        print('Woof')

class Cat(Animal):
    def make_sound(self) -> None:
        print('Meow')

class Cow(Animal):
    def make_sound(self) -> None:
        print('Mooo')

class Bird(Animal):
    def make_sound(self) -> None:
        print('Tweak')

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()
    
class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

class CowFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cow()
    

class BirdFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Bird()
    
class Factory:
    _factories: dict
    def __init__(self) -> None:
        self._factories={key : value for key, value in AnimalFactory._classes.items()}
    
    def create_animal(self, type_:str) -> Animal:
        return self._factories[type_]().create_animal()



def main():
    AnimalFactory.add_animal('dog', DogFactory)
    AnimalFactory.add_animal('cat', CatFactory)
    AnimalFactory.add_animal('cow', CowFactory)
    AnimalFactory.add_animal('bird', BirdFactory)
    factory = Factory()

    dog = factory.create_animal('dog')
    cat = factory.create_animal('cat')
    bird = factory.create_animal('bird')

    dog.make_sound()
    cat.make_sound()
    bird.make_sound()




if __name__ == "__main__":
    main()