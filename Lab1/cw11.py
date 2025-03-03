class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius) -> str:
        return f'{(celsius*(9/5))+32} °F'

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit) -> str:
        return f'{(fahrenheit-32)*(5/9)} °C'



def main():
    print(TemperatureConverter.celsius_to_fahrenheit(15))
    print(TemperatureConverter.fahrenheit_to_celsius(36))

if __name__ == '__main__':
    main()