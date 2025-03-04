from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self)->None:
        pass


class Piano(Instrument):
    def play(self)->str:
        return 'vanBeethoven'

class Guitar(Instrument):
    def play(self)->str:
        return 'Nirvana' 
    

def main():
    piano = Piano()
    guitar = Guitar()
    print(piano.play())
    print(guitar.play())


if __name__ == '__main__':
    main()
