class ElectricVehicle:
    def fuel_type(self)->str:
        return 'electric'
    
class GasolineVehicle:
    def fuel_type(self)->str:
        return 'gasoline'
    
class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self)->str:
        return 'hybrid'
    
def main():
    electric = ElectricVehicle()
    gasoline = GasolineVehicle()
    hybrid  = HybridCar()
    print(electric.fuel_type())
    print(gasoline.fuel_type())
    print(hybrid.fuel_type())
    
if __name__ == '__main__':
    main()
    
    
    