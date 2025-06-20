import json
from db import DatabaseSingleton, DB_PATH
from Book.services import BookService
from User.factory import StudentFactory, WorkerFactory
from Book.crud import BookCRUD
from User.crud import UserCRUD
from services import Services
from auth import login, register, clear_console
from Book.book_facade import ReserveFacade, BorrowFacade
from User.services import UserService
from Book.notifier import BookNotifier, initialize_notifier_from_db
from Notification.crud import NotificationCRUD
from User.memento import Memento
import auth 
import os
import json


if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w", encoding='utf8') as file:
        json.dump({"users":[], "books":[], "notifications":{}},file, ensure_ascii=False, indent= 4) 

db = DatabaseSingleton()
book_crud = BookCRUD(db)
user_crud = UserCRUD(db)
notifier = BookNotifier(book_crud)
notification_crud = NotificationCRUD(db)
memento = Memento()
initialize_notifier_from_db(book_crud, notifier, notification_crud)
book_service = BookService(book_crud, user_crud, notifier, notification_crud, memento)
user_service = UserService(db, user_crud)
book_return_facade = ReserveFacade(book_service, book_crud)
book_borrow_facade = BorrowFacade(book_service, book_crud)
services = Services(book_crud)

def main():
    clear_console()
    while True:
        if not auth.current_user:
            services.main_menu()
            choice = input("Wybierz opcję: ")
            clear_console()
            if choice == "1":
                user = login()
                if not user:
                    print("Logowanie nieudane")
            elif choice == "2":
                clear_console()
                services.register_menu()
                choice = input("Wybierz opcję: ")
                if choice == "1":
                    clear_console()
                    register(StudentFactory())
                elif choice == "2":
                    clear_console()
                    register(WorkerFactory())
                else:
                    continue
            elif choice == "3":
                print("Do widzenia!")
                break
            else:
                print("Niepoprawny wybór.")

        elif auth.current_user['role'] == "student":
            services.user_menu()
            choice = input("Wybierz opcję: ")
            clear_console()
            if choice == "1":
                book_service.show_books()
            elif choice == "2":
                clear_console()
                book = book_service.get_book() 
                if book:
                    services.book_details_user(int(book['id']))
                    choice = input("Wybierz opcję: ")
                    if book["is_available"]:
                        if choice == "1":
                            clear_console()
                            book_borrow_facade.borrow_book(int(book['id']))
                        elif choice == "2":
                             clear_console()
                             continue
                    else:
                        if choice =="1":
                            clear_console()
                            book_return_facade.reserve_book(int(book['id']))
                        elif choice == "2":
                            clear_console()
                            continue
                else:
                    continue
            elif choice == "3":
                clear_console()
                book_service.return_book()     
            elif choice == "4":
                clear_console()
                user_service.get_user_borrow_history(user['id']) 
            elif choice == "5":
                clear_console()
                user_service.get_user_return_history(user['id']) 
            elif choice == "6":
                book_service.undo_last_operation()       
            elif choice == "7":
                print("Do widzenia!")
                break
            else:
                print("Niepoprawny wybór.")
        else:
            services.worker_menu()
            choice = input("Wybierz opcje: ")
            if choice == "1":
                clear_console()
                book = book_service.show_books() 
            elif choice == "2":
                book = book_service.get_book() 
                if book: 
                    services.book_details_worker()
                    choice = input("Wybierz opcję: ") 
                    if choice == "1":
                        clear_console()
                        book_service.update_book(book)
                    if choice == "2":
                        book_service.delete_book(book)
                    if choice == "3":
                        clear_console()
                        continue
                else:
                    continue
            elif choice == "3":
                clear_console()
                book_service.create_book() 
            elif choice == "4":
                print("Do widzenia!") 
                break
            else:
                print("Niepoprawny wybór.")

       
if __name__ == "__main__":
    main()