from typing import Self
import sqlite3 


class Singleton:
    _instance: Self = None

    def __new__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance

        return cls._instance 
    
class DataBaseConnection(Singleton):
    def __init__(self, db_name: str = "test.db"):
        if not hasattr(self, "connection"):
            self.connection = sqlite3.connect(db_name)
            print(f"Połączono z bazą: {db_name}")

    def execute_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("Zapytanie wykonane")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Połączenie zamknięte")

    
def main():
    db1 = DataBaseConnection()
    db2 = DataBaseConnection()

    print(db1 is db2)

    db1.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR, email VARCHAR)')
    db1.execute_query("INSERT INTO users (name, email) VALUES ('Dawid', 'dawid@example.com')")
    db2.execute_query("INSERT INTO users (name, email) VALUES ('Arek', 'arek123@wp.pl')")
    #db2.execute_query("DELETE FROM users WHERE ID = 3")
    

    db1.close()

if __name__ == "__main__":
    main()