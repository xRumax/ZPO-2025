from .services import BookService
import auth
from .crud import BookCRUD

class ReserveFacade():
    def __init__(self, book_service: BookService, book_crud: BookCRUD) -> None:
        self.book_service = book_service
        self.book_crud = book_crud

    def reserve_book(self, book_id: int) -> bool:
        if auth.current_user is None:
            print("Musisz się zalogować!")
            return False
        
        book = self.book_crud.find_book_by_id(book_id)        
        user_id = auth.current_user['id']
        success = self.book_service.reserve_book(book_id, user_id)
        if success:
            print(f"Książka {book['name']} została zarezerwowana dla użytkownika {auth.current_user['name']} {auth.current_user['last_name']}")
        else:
            print("Rezerwacja nie powiodła się")
        return success
    
class BorrowFacade():
    def __init__(self, book_service: BookService, book_crud: BookCRUD) -> None:
        self.book_service = book_service
        self.book_crud = book_crud

    def borrow_book(self, book_id: int) -> bool:
        if auth.current_user is None:
            print("Musisz się zalogować!")
            return False
        
        book = self.book_crud.find_book_by_id(book_id)
        user_id = auth.current_user['id']
        success = self.book_service.borrow_book(book_id, user_id)
        if success:
            print(f"Książka {book['name']} została wypożyczona dla użytkownika {auth.current_user['name']} {auth.current_user['last_name']}")
        else:
            print("Wypożyczenie nie powiodło się")
        return success