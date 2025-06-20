from copy import deepcopy
from typing import Any

class Configuration:
    def __init__(self, email: str, region:str, language: str, password: str, darkmode: bool) -> None:
        self.email = email
        self.region = region
        self.language = language
        self.password = password
        self.darkmode = darkmode

    def get_info(self) -> None:
        for key, value in vars(self).items():
            print(f"{key} : {value}")

class Prototype:
    def __init__(self) -> None:
        self.objects = dict()
    
    def add_prototype(self, id_:Any, obj:Any) -> None:
        self.objects[id_] = obj
    
    def del_prototype(self, id_:Any) -> None:
        del self.objects[id_]

    def clone(self, id_: Any, **kwargs) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])
            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance
        
        else:
            ValueError("Object doesn't exist")

def main():
    config = Configuration('str@wp.pl', 'Poland', 'Polish', '1234', True)
    config.get_info()
    print()

    prototypes = Prototype()
    prototypes.add_prototype("1", config)

    another_config = prototypes.clone("1", email = "example@outlook.com", region= "Germany", name = "Piotrek")
    another_config.get_info()

if __name__ == "__main__":
    main()

