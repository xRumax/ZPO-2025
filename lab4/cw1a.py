from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def tax_deduction(self, amount):
        pass

class SpainTax(TaxStrategy):
    def tax_deduction(self, amount) -> float:
        return amount * 0.12

class PolandTax(TaxStrategy):
    def tax_deduction(self, amount) -> float:
        return amount * 0.23

class Taxer:
    def __init__(self, strategy: TaxStrategy)->None:
        self.strategy = strategy

    def show_taxes(self, amount: float) -> float:
        return self.strategy.tax_deduction(amount)


def main():
    spain = SpainTax()
    poland = PolandTax()

    taxer1 = Taxer(spain)
    taxer2 = Taxer(poland)

    print(taxer1.show_taxes(200))
    print(taxer2.show_taxes(200))

if __name__ == "__main__":
    main()

