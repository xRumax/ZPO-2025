from abc import ABC, abstractmethod

class BookDescriptionDecorator(ABC):
    def __init__(self, book:dict) -> None:
        self._book = book

    @abstractmethod
    def get_description(self) -> str:
        pass

class BasicBookDescription(BookDescriptionDecorator):        
    def get_description(self):
        return f""

class ReservedDecorator(BookDescriptionDecorator):
    def __init__(self, decorated: BookDescriptionDecorator) -> None:
        self._decorated = decorated

    def get_description(self):
        return f"{self._decorated.get_description()} [Zarezerwowana]"
    
class NewDecorator(BookDescriptionDecorator):
    def __init__(self, decorated: BookDescriptionDecorator) -> None:
        self._decorated = decorated

    def get_description(self):
        return f"{self._decorated.get_description()} [Nowość]"
    
class BestsellerDecorator(BookDescriptionDecorator):
    def __init__(self, decorated: BookDescriptionDecorator) -> None:
        self._decorated = decorated

    def get_description(self):
        return f"{self._decorated.get_description()} [Bestseller]"

class HITDecorator(BookDescriptionDecorator):
    def __init__(self, decorated: BookDescriptionDecorator) -> None:
        self._decorated = decorated

    def get_description(self):
        return f"{self._decorated.get_description()} [HIT]"