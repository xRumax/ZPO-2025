from services import Services
from User.factory import UserFactory
from db import DatabaseSingleton
from User.services import UserService
from Book.crud import BookCRUD
from Notification.crud import NotificationCRUD
from User.crud import UserCRUD
import os

db = DatabaseSingleton()
user_crud = UserCRUD(db)
user_services = UserService(db, user_crud) 
book_crud = BookCRUD(db)
services = Services(book_crud)
notification_crud = NotificationCRUD(db)
current_user = None

def login():
    global current_user
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    users = services.load_users()
    for user in users:
        if user['login'] == login:
            if user['password'] == password:
                clear_console()
                print(f"Zalogowano jako: {user['name']} {user['last_name']} ({user['role']})")
                notification_crud.display_pending_notification(user['id'])
                current_user = user
                return user
            else:
                print("Błędne hasło!")
                return None
    
    print("Nie znaleziono takiego użytkownika!")
    return None

def register(factory: UserFactory):
    id = len(user_services.get_users()) + 1
    name = str(input("Imię: "))
    last_name = str(input("Nazwisko: "))
    age = int(input("Wiek: "))
    login = input("Login: ")
    password = input("Hasło: ")
    user = factory.create_user(id = id, name=name, last_name=last_name, age=age, login=login, password=password)
    user_services.add_user(user.model_dump())
    print(f"Użytkownik {name} {last_name} został zarejestrowany.")


def clear_console():
    os.system('cls' if os.name == "nt" else "clear")