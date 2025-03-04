from abc import ABC, abstractmethod

class DatabaseConnection:
    @abstractmethod
    def connection(self) -> None:
        pass

    @abstractmethod
    def execute_query(self) -> None:
        pass


class MySQLConnection(DatabaseConnection):
    def connection(self) -> str:
        return f"Connected to MySQL database"

    def execute_query(self, query: str) -> None:
        return f"The query: {query} was made successfully in MySQL"

class PostgreSQLConnection(DatabaseConnection):
    def connection(self) -> str:
        return f"Connected to PostgreSQL database"

    def execute_query(self, query: str) -> None:
        return f"The query: {query} was made successfully in PostgreSQL"
    

def main():
    mysql = MySQLConnection()
    postgre = PostgreSQLConnection()
    print(mysql.connection())
    print(mysql.execute_query('POST'))
    print(postgre.connection())
    print(postgre.execute_query('GET'))


if __name__ == '__main__':
    main()

