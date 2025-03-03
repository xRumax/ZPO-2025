

class Employee():    
    def __init__ (self, first_name:str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Manager(Employee):
    def __init__(self, first_name:str, last_name: str, salary:float, departament: str ) -> None:
        super().__init__(first_name, last_name, salary)
        self.departament = departament

    def get_departament_info(self)-> str:
        return f'{self.departament}'
    

def main():
    employee = Employee('Marek', 'Nowak', 15250)
    manager = Manager('Paweł', 'Dąbrowski', 26100, 'IT')
    print(employee.get_full_name())
    print(manager.get_departament_info())
    print(manager.get_full_name())


if __name__ == '__main__':
    main()