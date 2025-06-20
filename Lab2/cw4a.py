from copy import deepcopy
from typing import Any

class Character:
    def __init__(self, name:str, health:int, mana:int, exp:int, damage:int, shield:int, skills: list) -> None:
        self.name = name
        self.health = health
        self.mana = mana
        self.exp = exp
        self.damage = damage
        self.shield = shield
        self.skills = skills

    
    def get_info(self) -> None:
        for key, value in vars(self).items():
            print(f"{key} : {value}")



class Prototype:
    def __init__(self) -> None:
        self.objects = dict()
    
    def add_prototype(self, id_:Any, obj: Any) -> None:
        self.objects[id_] = obj
    
    def get_prototype(self, id_:Any) -> None:
        del self.objects[id_]
    
    def clone(self, id_:Any, **kwargs) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance
        else:
            return ValueError("Prototype doesn't exist")


def main():
    mage = Character("Yennefer", 100, 150, 200, 50, 10, ['fireball', 'iceball'])
    mage.get_info() 

    prototypes = Prototype()
    prototypes.add_prototype("1", mage)
    warrior = prototypes.clone("1", name="Geralt", health=200, mana=100, exp=300, damage=100, shield=20, skills=['aksji', 'yrden', 'aard','igni', 'quen'])
    print()
    warrior.get_info()
    

if __name__ == "__main__":
    main()