from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Role(str, Enum):
    student = "student"
    pracownik = "pracownik"
    admin = "admin"


class User(BaseModel):
    id: int
    name: str
    last_name: str
    age: int
    login: str
    password: str
    reserved_books: Optional[list[str]] = []
    borrowed_books: Optional[list[str]] = []
    borrow_history: Optional[list[str]] = []
    return_history: Optional[list[str]] = []
    role: Role

class Worker(BaseModel):
    id: int
    name: str
    last_name: str
    age: int
    login: str
    password: str
    role: Role

class Student(Worker):
    reserved_books: Optional[list[str]] = []
    borrowed_books: Optional[list[str]] = []
    borrow_history: Optional[list[str]] = []
    return_history: Optional[list[str]] = []
