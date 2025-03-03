class GameCharacter:
    default_health=100

    def restore_health(self) -> None:
        self.default_health = 100

    @classmethod
    def set_default_health(cls, new_value) -> None:
        cls.default_health = new_value



def main():
    geralt = GameCharacter()
    print(geralt.default_health)
    #Zmiana domyślnej wartości zdrowia ze 100 na 200 dla nowych postaci
    GameCharacter.set_default_health(200)

    obj = GameCharacter()
    print(obj.default_health)

    GameCharacter.set_default_health(400)
    obj2 = GameCharacter()
    print(obj2.default_health)
    obj2.restore_health()
    print(obj2.default_health)



if __name__ == '__main__':
    main()