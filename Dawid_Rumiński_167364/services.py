from db import DatabaseSingleton
import json
from Book.crud import BookCRUD

db = DatabaseSingleton()

class Services:
    def __init__(self, book_crud: BookCRUD) -> None:
        self.book_crud = book_crud

    def load_users(self):
        with open("./Projekt/data.json", "r", encoding='utf8') as file:
            data = json.load(file)
        return data['users']

    def main_menu(self):
        print("\n== MENU ==")
        print("1. Logowanie")
        print("2. Rejestracja")
        print("3. Wyjdź")

    def register_menu(self):
        print("\n== REJESTRACJA ==")
        print("Kto chcę się zarejestrować?")
        print("1. Student")
        print("2. Pracownik")
        print("3. Cofnij")

    def user_menu(self):
        print("\n== WITAJ W BIBLIOTECE ==")
        print("1. Pokaż listę książek")
        print("2. Wyszukaj książkę")
        print("3. Zwróć książkę")
        print("4. Wyświetl historię wypożyczeń")
        print("5. Wyświetl historię zwrotów")
        print("6. Cofnij ostatnią akcję")
        print("7. Wyloguj")

    def worker_menu(self):
        print("\n== WITAJ W BIBLIOTECE ==")
        print("1. Pokaż listę książek")
        print("2. Wyszukaj książkę")
        print("3. Dodaj pozycję")
        print("4. Wyloguj")

    def book_details_user(self, book_id:int):
        book = self.book_crud.find_book_by_id(book_id)
        if book['is_available'] == True:
            print("\n== OPCJE ==")
            print("1. Wypożycz książkę")
            print("2. Wróć")
        else:
            print("\n== OPCJE ==")
            print("1. Zarezerwuj książkę")
            print("2. Wróć")

    def book_details_worker(self):
        print("\n== OPCJE ==")
        print("1. Edytuj pozycję")
        print("2. Usuń pozycję")
        print("3. Wróć")
