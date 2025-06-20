from copy import copy, deepcopy
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

class Mage(Character):
    def __init__(self, name: str, health: int, mana: int, exp: int, damage: int, shield: int, skills: list) -> None:
        super().__init__(name, health, mana, exp, damage, shield, skills)


class Prototype:
    def __init__(self) -> None:
        self.objects = dict()
    
    def add_prototype(self, id_:Any, obj: Any) -> None:
        self.objects[id_] = obj
    
    def get_prototype(self, id_:Any) -> None:
        del self.objects[id_]
    
    def clone(self, id_:Any, **kwargs) -> Any:
        if id_ in self.objects:
            instance = copy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance
        else:
            return ValueError("Prototype doesn't exist")
        
    def deepclone(self, id_: Any, **kwargs) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance


def main():
    mage = Mage("Yennefer", 100, 150, 200, 50, 10, ['fireball', 'iceball'])

    prototypes = Prototype()
    prototypes.add_prototype("1", mage)
    warrior_deep = prototypes.deepclone("1", name="Geralt")
    warrior = prototypes.clone("1", name="Geralt")
    mage.skills.append('axii')

    # shallow copy
    print("Shallow copy:")
    print("Mage's skills: ", mage.skills)    
    print("Warrior's skills (shallow): ", warrior.skills)

    # deepcopy
    print("\nDeepcopy:")
    print("Mage's skills: ", mage.skills)    
    print("Warrior's skills (deep): ", warrior_deep.skills)

    

if __name__ == "__main__":
    main()