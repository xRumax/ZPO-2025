from __future__ import annotations

class Degrees:
    def __init__(self, degrees: float) -> None:
        self.degrees = degrees

class FahrenheitSensor:
    def __init__(self, fahrenheit: Fahrenheit) -> None:
        self.fahrenheit = fahrenheit

    def convert_faren_to_celsious(self) -> float:
        return (self.fahrenheit.degrees-32) * 5/9

class Celsious(Degrees):
    def celsious_degrees(self) -> float:
        return self.degrees

class Fahrenheit(Degrees):
    def fahrenheit_degrees(self) -> float:
        return self.degrees

class AdapterCelsious:
    def __init__(self, fahrenheitSensor: FahrenheitSensor) -> None:
        self.fahrenheitSensor = fahrenheitSensor

    def celsious_degrees(self) -> float:
        return self.fahrenheitSensor.convert_faren_to_celsious()

def main():
    celsious = Celsious(32)
    fahrenheit = Fahrenheit(52)
    fahrenheitSensor = FahrenheitSensor(fahrenheit)

    print(celsious.celsious_degrees())
    adaptered_cel = AdapterCelsious(fahrenheitSensor)
    print(adaptered_cel.celsious_degrees())
if __name__ == "__main__":
    main()