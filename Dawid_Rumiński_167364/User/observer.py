from abc import ABC, abstractmethod
from Book.crud import BookCRUD
from Notification.crud import NotificationCRUD  
import auth

class Observer(ABC):
    @abstractmethod
    def notify(self, book_id: int) -> None:
        pass

class UserObserver(Observer):
    def __init__(self, user_id: int, book_crud: BookCRUD, notification_crud: NotificationCRUD):
        self.user_id = user_id
        self.book_crud = book_crud
        self.notification_crud = notification_crud

    def notify(self, book_id: int) -> None:
        book = self.book_crud.find_book_by_id(book_id)
        message = f"Użytkownik {self.user_id}: Książka {book['name']} jest już dostępna!"
        if auth.current_user and auth.current_user['id'] == self.user_id:
            print(message)
        else:
            self.notification_crud.add_notification(self.user_id, message)