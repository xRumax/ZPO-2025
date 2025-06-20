from typing import Any


class BookCRUD:
    def __init__(self, db:Any) -> None:
        self.db = db

    def get_books(self) -> list:
        data = self.db.load_data()
        return data['books']

    def add_book(self, book: Any) -> None:
        data=self.db.load_data()
        data['books'].append(book)
        self.db.save_data(data)

    def edit_book(self, updated_book:Any) -> None: 
        data=self.db.load_data()
        for i, book in enumerate(data['books']):
            if book['id'] == updated_book['id']:
                data['books'][i] = updated_book
                break
        self.db.save_data(data)
    
    def find_book_by_id(self, id:int) -> dict | None:
        data = self.db.load_data()
        for book in data['books']:
            if book['id'] == id:
                return book
        return None

    def delete_book(self, book_id:int) -> bool:
        data = self.db.load_data()
        for book in data['books']:
            if book_id == book['id']:
                data['books'].remove(book)
                self.db.save_data(data)
                return True
        return False
