from collections import namedtuple

Transaction = namedtuple("Transaction",['transaction_id', 'amount', 'currency'])

class BankAccount():
    def __init__(self, balance: float) -> None:
        self.balance = balance


    def apply_transaction(self, transaction: Transaction)-> None:
        self.balance += transaction.amount

    def get_balance(self) -> float:
        return self.balance
    

def main():
    account = BankAccount(10)
    print(account.get_balance())
    transaction = Transaction(1, 100, 'PLN')
    account.apply_transaction(transaction)
    print(account.get_balance())

if __name__ == '__main__':
    main()