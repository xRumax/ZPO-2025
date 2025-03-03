from datetime import date

class Car:
    brand:str
    model:str
    year:int
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def is_classic(self) -> bool:
        if (date.today().year -self.year) > 25:
            return True
        return False


def main():
    car = Car('Volkswagen', 'Passat', 1999)
    car2 = Car('Skoda', 'Octavia', 2014)
    print(car.is_classic())
    print(car2.is_classic())

if __name__ == '__main__':
    main()