from abc import ABC, abstractmethod 

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self) -> None:
        pass

    @abstractmethod
    def capture_payment(self) -> None:
        pass

class CredidCardPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "The transaction has been authorized"
        
    def capture_payment(self, amount:float) -> str:
        return f"The amount downloaded from your account is {amount} PLN."
    
class PayPalPayment(PaymentProcessor):
    def __init__(self, balance:float) -> None:
        self.balance = balance

    def authorize_payment(self) -> str:
        return "The transaction has been authorized"
        
    def capture_payment(self, amount:float) -> str:
        self.balance = self.balance - amount
        return (f"Download of PayPal payments in the amount {amount} PLN."
        f"Your account balance is now: {self.balance}")
    


def main():
    card = CredidCardPayment()
    print(card.capture_payment(200))

    paypal = PayPalPayment(3000)
    print(paypal.balance)
    print(paypal.capture_payment(200))
    print(paypal.balance)


if __name__ == '__main__':
    main()