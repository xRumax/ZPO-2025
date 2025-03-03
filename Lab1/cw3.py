from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, discount: float) -> float:
        return self.price * (1 - (discount*0.01))

def main():
    book = Book('Wiedźmin: Ostatnie Życzenie', 'Andrzej Sapkowski', 1993, 49.90)
    print(book.apply_discount(50))
    


if __name__ == '__main__':
    main()