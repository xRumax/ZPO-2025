from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod 
    def add_part(self, part:str) -> None:
        pass

    @abstractmethod
    def get_result(self) -> None:
        pass

class Pizza:
    def __init__(self) -> None:
        self._parts = []

    def add(self, part:str) -> None:
        self._parts.append(part)

    def list_parts(self) ->None:
        print(f"Pizza parts: {', '.join(self._parts)}")

    
class MeatBuilder(Builder):
    def __init__(self) -> None:
        self._pizza = Pizza()
    
    def add_part(self, part:str)->None:
        self._pizza.add(part)

    def get_result(self) -> Pizza:
        return self._pizza

class MargharitaBuilder(Builder):
    def __init__(self) -> None:
        self._pizza = Pizza()
    
    def add_part(self, part:str)->None:
        self._pizza.add(part)

    def get_result(self) -> Pizza:
        return self._pizza


class VegeBuilder(Builder):
    def __init__(self) -> None:
        self._pizza = Pizza()
    
    def add_part(self, part:str)->None:
        self._pizza.add(part)

    def get_result(self) -> Pizza:
        return self._pizza


class Director:
    def __init__(self) ->None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def make_vege(self) -> None:
        self.builder.add_part('Mozzarella')
        self.builder.add_part('Tomato')
        self.builder.add_part('Pieapple')
        self.builder.add_part('Onion')

    def make_meat(self) -> None:
        self.builder.add_part('Mozzarella')
        self.builder.add_part('Salami')
        self.builder.add_part('Ham')
        self.builder.add_part('Chili')
        self.builder.add_part('Onion')

    def make_margharita(self) -> None:
        self.builder.add_part('Mozzarella')
        self.builder.add_part('Tomato')
        self.builder.add_part('Gouda')
        self.builder.add_part('Basil')
    

def main():
    director = Director()

    #Vege pizza
    vege_builder = VegeBuilder()
    director.builder = vege_builder
    director.make_vege()
    pizza = vege_builder.get_result()
    print('Vege pizza: ')
    pizza.list_parts()

    #Meat pizza
    meat_builder = MeatBuilder()
    director.builder = meat_builder
    director.make_meat()
    pizza = meat_builder.get_result()
    print('Meat pizza: ')
    pizza.list_parts()

    #Margharita pizza
    margharita_builder = MargharitaBuilder()
    director.builder = margharita_builder
    director.make_margharita()
    pizza = margharita_builder.get_result()
    print('Margharita pizza: ')
    pizza.list_parts()

if __name__ == "__main__":
    main() 




