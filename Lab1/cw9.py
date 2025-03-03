class FlyingVehicle:
    def move(self) -> str:
        return 'I fly'
    
class WaterVehicle:
    def move(self) -> str:
        return 'I sail'

class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    def __init__(self, mode: str = 'Flying') -> None:
        self.mode = mode
    
    def move(self) -> str:
        if self.mode == 'Flying':
            return super().move()
        elif self.mode == 'Water': 
            return 'I sail'


def main():
    flight = FlyingVehicle()
    boat = WaterVehicle()
    amphibious = AmphibiousVehicle("Water")
    print(flight.move())
    print(boat.move())
    print(amphibious.move())

if __name__ == '__main__':
    main()