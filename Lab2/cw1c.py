from abc import ABC, abstractmethod

class ComputerManually:
    def __init__(self, cpu: str, gpu: str, ram: str, storage: str, os:str) -> None:
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.os = os

    def __str__(self) -> str:
        return f"Computer specs: CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Storage: {self.storage}, OS: {self.os}"
    

class Builder(ABC):
    @abstractmethod
    def set_cpu(self) -> None:
        pass
    
    @abstractmethod
    def set_gpu(self) -> None:
        pass

    @abstractmethod
    def set_ram(self) -> None:
        pass
    
    @abstractmethod    
    def set_storage(self) -> None:
        pass

    @abstractmethod    
    def set_os(self) -> None:
        pass

class Computer:
    def __init__(self) -> None:
        self._parts =[]

    def add(self, part:str) -> None:
        self._parts.append(part)

    def list_parts(self) -> None:
        print(f"Computer parts: {', '.join(self._parts)}")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def make_gaming(self) -> None:
        self.builder.set_cpu()
        self.builder.set_gpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_os()


class GamingComputer(Builder):
    def __init__(self) -> None:
        self._computer = Computer()

    def set_cpu(self) -> None:
        self._computer.add('i9 14700HX')
    
    def set_gpu(self) -> None:
        self._computer.add('RTX 5090')
    
    def set_ram(self) -> None:
        self._computer.add('32GB')

    def set_storage(self) -> None:
        self._computer.add('1TB')
    
    def set_os(self) -> None:
        self._computer.add('Windows')

    def get_result(self) -> Computer:
        return self._computer



def main():
    computer = ComputerManually("i7", "GTX 1080", "16GB", "1TB", "Windows")
    print(computer)

    director = Director()

    gaming_builder = GamingComputer()
    director.builder = gaming_builder
    director.make_gaming()
    computer = gaming_builder.get_result()
    computer.list_parts()

if __name__ == "__main__":
    main() 