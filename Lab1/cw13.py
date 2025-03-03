class Store:
    total_customers = 0

    def add_customer(self, customers: int) -> None:
        Store.total_customers += customers

    
    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers


def main():
    store=Store()
    store.add_customer(15)
    print(store.get_total_customers())

    store2=Store()
    store2.add_customer(35)
    print(store2.get_total_customers())
    print(Store.get_total_customers())

if __name__ == '__main__':
    main()