from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    category: str = field(default='General')

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("The price must be greater than 0")
    

def main():
    product = Product('ziemniaki', 20)
    print(product)

if __name__ == '__main__':
    main()