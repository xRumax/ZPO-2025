from .crud import BookCRUD
from .models import Book
from typing import Any
from User.crud import UserCRUD
from User.observer import UserObserver
from .notifier import BookNotifier
from Notification.crud import NotificationCRUD
from User.memento import Memento
from .describe import BasicBookDescription, ReservedDecorator, NewDecorator, BestsellerDecorator
from rich.console import Console
from rich.table import Table
from datetime import datetime
import auth
import json


class BookService:
    def __init__(self, book_crud: BookCRUD, user_crud: UserCRUD, notifier: BookNotifier, notification_crud : NotificationCRUD, memento: Memento)->None:
        self.book_crud = book_crud   
        self.user_crud = user_crud
        self.notifier = notifier
        self.notification_crud = notification_crud 
        self.memento = memento

    def create_book(self) -> None:
        books = self.book_crud.get_books()
        if books:
            id = max(book['id'] for book in books) + 1
        else:
            id = 1
        isbn = int(input("ISBN: "))
        name = str(input("Tytuł: "))
        author = str(input("Autor: "))
        year = int(input("Rok wydania: "))
        genre = str(input("Gatunek: "))
        book = Book(id= id, isbn = isbn, name = name, author= author, year=year, genre = genre)
        self.book_crud.add_book(book.model_dump())
        print(f"Książka: {name} Autora: {author} została pomyślnie dodana.")

    def delete_book(self, book:Any) -> str:
        if book:
            self.book_crud.delete_book(book['id'])
            print(f"{book['name']}\n Została pomyślnie usunięta z bazy!")
        else:
            print("Nie znaleziono książki")
        
    def show_books(self) -> list:
        books = self.book_crud.get_books()
        
        table = Table(title = "Lista Książek")
        table.add_column("Lp", justify="center", no_wrap=True)
        table.add_column("ID", justify="center")
        table.add_column("Tytuł", justify="center")
        table.add_column("Autor", justify="center")
        table.add_column("Dostępność", justify="center")
        table.add_column("Opis", justify="center", style ="Yellow")


        for i, book in enumerate(books, start = 1):
            description = BasicBookDescription(book)

            if book['reservation_queue'] and len(book['reservation_queue']) >0:
                description = ReservedDecorator(description)

            if int(book['year']) >= 2024:
                description = NewDecorator(description)
            
            if book['genre'] == "Kryminał":
                description = BestsellerDecorator(description)
            availability_status = "Dostępna" if book['is_available'] else "Niedostępna"
            table.add_row(str(i), str(book['id']), str(book['name']), str(book['author']), availability_status, description.get_description())
        console = Console()
        console.print(table)
        return books

    def get_book(self) -> dict|None:
        book_id = int(input("Podaj id książki, którą chcesz wyszukać: "))
        auth.clear_console()
        book = self.book_crud.find_book_by_id(book_id)
        table = Table(title = "Książka")
        table.add_column("ID", justify="center")
        table.add_column("ISBN", justify="center")
        table.add_column("Tytuł", justify="center")
        table.add_column("Autor", justify="center")
        table.add_column("Rok", justify="center")
        table.add_column("Gatunek", justify="center")
        table.add_column("Dostępność", justify="center")
        table.add_column("Kolejka rezerwacji", justify="center")
        
        if book:
            availability_status = "Dostępna" if book['is_available'] else "Niedostępna"
            table.add_row(str(book['id']),str(book['isbn']), str(book['name']), str(book['author']), str(book['year']), str(book['genre']), availability_status, str(book['reservation_queue']))
            console = Console()
            console.print(table)
            return book
        else:
            print("Nie ma takiej książki!")
            return None
        

    def update_book(self, book: Any) -> None:
        isbn= str(input("Nowy numer ISBN: ")) or book['isbn']
        name = str(input("Nowy tytuł: ")) or book['name']
        author = str(input("Nowy autor: ")) or book['author']
        year = str(input("Rok: ")) or book['year']
        genre = str(input("Nowy gatunek: ")) or book['genre']
        book['isbn'] = isbn
        book['name'] = name
        book['author'] = author
        book['year'] = year
        book['genre'] = genre

        self.book_crud.edit_book(book)
        print('Książka została zaktulizowana')
        
    def reserve_book(self, book_id: int, user_id: int) -> bool:
        book = self.book_crud.find_book_by_id(book_id)
        user = self.user_crud.find_user_by_id(user_id)
        if not book:
            return False
        if book['is_available']:
            return False

        reservation_queue = book.get("reservation_queue", [])
        if user_id not in reservation_queue:
            reservation_queue.append(user_id)
            book['reservation_queue'] = reservation_queue
        self.book_crud.edit_book(book)

        if user:
            reserved_books = user.get("reserved_books", [])
            if book_id not in reserved_books:
                reserved_books.append(book_id)
                user['reserved_books'] = reserved_books
                self.user_crud.edit_user(user) 

                observer = UserObserver(user['id'], self.book_crud, self.notification_crud)
                self.notifier.add_observers(book_id, observer)
        return True
    
    def borrow_book(self, book_id: int, user_id: int) -> bool:
        book = self.book_crud.find_book_by_id(book_id)
        user = self.user_crud.find_user_by_id(user_id)
        if not book:
            return False
        if not book['is_available']:
            return False
        
        state = {
            "book" : book.copy(),
            "user": user.copy()
        }
        self.memento.save_state(json.dumps(state))

        book['is_available'] = False
        book['borrowed_by'] = user['id']

        user_borrow_history = user.get("borrow_history", [])
        current_time = datetime.now().isoformat()
        user_borrow_history.append([book_id, current_time])
        user["borrow_history"] = user_borrow_history

        if user_id in book['reservation_queue']:
            book['reservation_queue'].remove(user_id)

        self.book_crud.edit_book(book)

        if book_id in user['reserved_books']:
            user['reserved_books'].remove(book_id)

        borrowed_books = user.get("borrowed_books", [])
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            user['borrowed_books'] = borrowed_books
        self.user_crud.edit_user(user) 
        return True
    

    def return_book(self) -> None:
        if auth.current_user is None:
            print("Musisz się zalogować!")
            return

        user = self.user_crud.find_user_by_id(auth.current_user['id'])
        borrowed_books = user.get('borrowed_books', [])

        if not borrowed_books:
            print("Nie masz żadnej wypożyczonej książki")
            return
        
        print("\n== KSIĄŻKI DO ZWROTU ==")
        for i, book_id in enumerate(borrowed_books, start = 1):
            book = self.book_crud.find_book_by_id(book_id)
            if book:
                print(f"{i}.ID: {book['id']}, Tytuł: {book['name']}")

        try:
            choice = int(input("Podaj numer książki, którą chcesz zwrócić: ")) - 1
            if choice < 0 or choice >= len(borrowed_books):
                print("Niepoprawny wybór")
                return
        except:
            print("Niepoprawny wybór")
            return
        
        returned_book_id = borrowed_books[choice]
        book = self.book_crud.find_book_by_id(returned_book_id)
        if not book:
            print("Nie znaleziono książki")
            return
        
        state = {
            "book" : book.copy(),
            "user": user.copy()
        }
        self.memento.save_state(json.dumps(state))

        borrowed_books.remove(returned_book_id)
        user['borrowed_books'] = borrowed_books
        self.user_crud.edit_user(user)

        book['is_available'] = True
        book['borrowed_by'] = None
        user_return_history = user.get("return_history", [])
        current_time = datetime.now().isoformat()
        user_return_history.append([returned_book_id, current_time])
        user["return_history"] = user_return_history
        self.book_crud.edit_book(book)
        self.user_crud.edit_user(user)
        self.notifier.notify(book['id'])
        print(f"Książka {book['name']} została zwrócona")
        

    def undo_last_operation(self) -> None:
        last_state = self.memento.read_state()
        if not last_state:
            print("Brak zapisanych stanów do przywrócenia")
            return
        
        self.memento.undo()

        last_create_state = json.loads(last_state)
        restored_book = last_create_state.get("book")
        restored_user = last_create_state.get("user")
        if restored_book:
            self.book_crud.edit_book(restored_book)
        if restored_user:
            self.user_crud.edit_user(restored_user)
        print("Ostatnia operacja została cofnięta")