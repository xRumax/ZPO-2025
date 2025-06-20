from abc import ABC
from typing import Any
from .crud import BookCRUD
from User.observer import UserObserver
from Notification.crud import NotificationCRUD

class Observable(ABC):
    _observers: dict

    def __init__(self)->None:
        self._observers = {}

    def add_observers(self, book_id: int, observer: Any) -> None:
        self._observers.setdefault(book_id, []).append(observer)

    def delete_observer(self, book_id:int, observer: Any) -> None:
        if book_id in self._observers:
            self._observers[book_id].remove(observer)

    def notify(self, book_id:int) -> None:
        if book_id in self._observers and self._observers[book_id]:
            observer = self._observers[book_id].pop(0)
            observer.notify(book_id=book_id)

            if not self._observers[book_id]:
                del self._observers[book_id]


class BookNotifier(Observable):
    def __init__(self, book_crud: BookCRUD):
        super().__init__()
        self.book_crud = book_crud


def initialize_notifier_from_db(book_crud: BookCRUD, notifier: BookNotifier, notification_crud: NotificationCRUD):
    books = book_crud.get_books()
    for book in books:
        queue = book.get("reservation_queue", [])
        for user_id in queue:
            observer = UserObserver(user_id, book_crud, notification_crud)
            notifier.add_observers(book["id"], observer)

    