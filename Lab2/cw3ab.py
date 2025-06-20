from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_model(self) -> str:
        pass

class SUV(Car):
    def __init__(self, model:str):
        self.model = model

    def get_model(self) -> str:
        return f"SUV:{self.model}"


class Sedan(Car):
    def __init__(self, model:str):
        self.model = model

    def get_model(self) -> str:
        return f"Sedan:{self.model}"
    
class HatchbackCar(Car):
    def __init__(self, model:str):
        self.model = model

    def get_model(self) -> str:
        return f"Hatchback:{self.model}"
# ------------------------------------------
class Factory(ABC):
    @abstractmethod
    def create_suv(self) -> None:
        pass

    @abstractmethod
    def create_sedan(self) -> None:
        pass

    @abstractmethod
    def create_hatchback(self) -> None:
        pass

# ------------------------------------------
class TeslaFactory(Factory):
    def create_suv(self):
        return list(['Model X', 'Model Y'])
    
    def create_sedan(self):
        return list(['Model S', 'Model 3'])
    
    def create_hatchback(self):
        return list(['Model H3', 'Model H5' ])

class BMWFactory(Factory):
    def create_suv(self):
        return list(['X5', 'X6'])
    
    def create_sedan(self):
        return list(['M5', 'M3'])
    
    def create_hatchback(self):
        return list(['Seria 1', '316'])
# ------------------------------------------


class AbstractFactory:
    @staticmethod
    def get_factory(model:str):
        match model:
            case 'Tesla':
                return TeslaFactory()
            case 'BMW':
                return BMWFactory()
            case _:
                raise ValueError('Unknown Factory')
            

def main():
    factory_tesla= AbstractFactory.get_factory('Tesla')
    for brand in ['Tesla', 'BMW']:
        factory = AbstractFactory.get_factory(brand)
        suv_models = factory.create_suv()
        sedan_models = factory.create_sedan()
        hatchback_models = factory.create_hatchback()
        print(f"{brand} SUVs: {suv_models}")
        print(f"{brand} Sedans: {sedan_models}")
        print(f"{brand} Hatchbacks: {hatchback_models}")
    print(factory_tesla.create_hatchback()[0])
if __name__ == '__main__':
    main()