from .models import User, Student, Worker
from abc import ABC, abstractmethod


class UserFactory(ABC):
    @abstractmethod
    def create_user(self, id: int, name: str, last_name: str, age: int, login: str, password: str) -> User:
        pass

class StudentFactory(UserFactory):
    def create_user(self, id: int, name: str, last_name: str, age: int, login: str, password: str) -> User:
        return Student(id = id, name = name, last_name=last_name, age=age, login=login, password=password,  role ="student")
    
class WorkerFactory(UserFactory):
    def create_user(self, id: int, name: str, last_name: str, age: int, login: str, password: str) -> User:
        return Worker(id = id, name = name, last_name=last_name, age=age, login=login, password=password,  role ="pracownik")

