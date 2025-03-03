from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self)->None:
        pass


class Piano(Instrument):
    def play(self)->str:
        return 'sadfasdf'

class Guitar(Instrument):
    def play(self)->int:
        return 3 