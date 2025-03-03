class IDGenerator:
    _last_id = 0

    @classmethod
    def generate_id(cls) -> int:
        cls._last_id +=1 
        return cls._last_id

    def __init__(self) -> None:
        self.id = IDGenerator.generate_id()


def main():
    object1 = IDGenerator()
    object2 = IDGenerator()
    object3 = IDGenerator()
    print(object1.id)
    print(object2.id)
    print(object3.id)

if __name__ == '__main__':
    main()