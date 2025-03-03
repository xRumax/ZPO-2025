class Animal:
    def make_sound(self) -> str:
        return 'Some sound'


class Pet: 
    def is_domestic(self) -> bool:
        return True
    
class Dog(Animal, Pet):
    def make_sound(self):
        return 'Hau Hau'



def main():
    dog = Dog()
    print(dog.make_sound())
    print(dog.is_domestic())

if __name__ == '__main__':
    main()