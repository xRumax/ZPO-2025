from abc import ABC, abstractmethod

class CharacterStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass

class Defender(CharacterStrategy):
    skill : str = "Defend"
    def attack(self) -> str:
        return f"Character special is: {self.skill}"


class Support(CharacterStrategy):
    skill : str = "Healing"
    def attack(self) -> str:
        return f"Character special is: {self.skill}"
    
class Attacker(CharacterStrategy):
    skill : str = "Fire ball"
    def attack(self) -> str:
        return f"Character special is: {self.skill}"


class CharacterChoose:
    def __init__(self, name: str, character: CharacterStrategy):
        self.name = name
        self.character = character

    def use_strategy(self) -> str:
        return self.character.attack()


def main():
    defe = Defender()
    atack = Attacker()
    
    choose_character = CharacterChoose('Aurelion',defe)
    choose_character2 = CharacterChoose('Aatrox',atack)

    print(choose_character.use_strategy())
    print(choose_character2.use_strategy())


if __name__ == "__main__":
    main()