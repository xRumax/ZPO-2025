from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

    @abstractmethod
    def check_transaction_status(self, transaction_id: str) -> str:
        pass


class PayPal:
    def send_money(self, amount: float) -> None:
        print(f"User send {amount} PLN")

    def get_status(self, transaction_id: str) -> str:
        return f"Payment {transaction_id} completed"
    

class Stripe:
    def charge(self, amount:float) -> None:
        print(f"The fee has been made. Charge: {amount}")

    def get_charge_status(self,charge_id:str) -> str:
        return f"The charge with id: {charge_id} | completed"

class PaypalAdapter(PaymentGateway):
    def __init__(self, paypal:PayPal) -> None:
        self.paypal = paypal

    def process_payment(self, amount) -> None:
        self.paypal.send_money(amount)

    def check_transaction_status(self, transaction_id) -> str:
        return self.paypal.get_status(transaction_id)

class StripeAdapter(PaymentGateway):
    def __init__(self, stripe:Stripe)-> None:
        self.stripe = stripe

    def process_payment(self, amount)->None:
        self.stripe.charge(amount)
    
    def check_transaction_status(self, transaction_id) -> str:
        return self.stripe.get_charge_status(transaction_id)



class Payment:
    @staticmethod
    def get_payment_type(type:str) -> Any:
        match type:
            case "Paypal":
                return PaypalAdapter(PayPal())
            case "Stripe":
                return StripeAdapter(Stripe())
            case _:
                return ValueError("This type doesnt exist")
            
def main():

    adapterPay = Payment()
    paypal = adapterPay.get_payment_type("Paypal")
    paypal.process_payment(2000)
    status = paypal.check_transaction_status("XDWM42QP")
    print(status)
 

if __name__ == "__main__":
    main()