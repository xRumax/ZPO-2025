from abc import ABC, abstractmethod

class DeliverProcessor(ABC):


    @abstractmethod
    def set_delivery(self) -> None:
        pass

    @abstractmethod
    def payment(self)->None:
        pass

    def prepare_package(self) ->None:
        print("Preparation of the package in progress...")

    def pack(self) -> None:
        print("The package is packed...")

    def send(self) -> None:
        print("The package was sent")
          
    def run(self) -> None:
        self.set_delivery()
        self.payment()
        self.prepare_package()
        self.pack()
        self.send()


class ExpressDelivery(DeliverProcessor):
    def set_delivery(self)->None:
        print("You chose a Express Delivery")

    def payment(self) -> None:
        print("Card payment on the Internet")

class ClassicDelivery(DeliverProcessor):
    def set_delivery(self) -> None:
        print("You chose a Classic Delivery")
    
    def payment(self) -> None:
        print("BLIK transfer on the Internet")

class PersonalPickup(DeliverProcessor):
    def set_delivery(self) -> None:
        print("You chose a Personal Pickup")
    
    def payment(self) ->None:
        print("Cash payment on site")

def main():
    processor = [ExpressDelivery(),
                 ClassicDelivery(),
                 PersonalPickup()]
    
    for process in processor:
        process.run()
        print('\n')

if __name__ == "__main__":
    main()
