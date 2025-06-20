from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def control(self):
        pass

class Television(Device):
    def control(self) -> None:
        print("You control TV now")

class Radio(Device):
    def control(self) -> None:
        print("You control Radio now")

class Drone(Device):
    def control(self) -> None:
        print("You control Drone now")

class Remote(ABC):
    def __init__(self, device: Device) -> None:
        self.device = device

    @abstractmethod
    def control_device(self):
        pass 

class RemoteControl(Remote):

    def control_device(self):
        self.device.control()


def main():
    dev = RemoteControl(Television())
    dev2 = RemoteControl(Radio())
    dev3 = RemoteControl(Drone())

    dev.control_device()
    dev2.control_device()
    dev3.control_device()

if __name__ == "__main__":
    main()