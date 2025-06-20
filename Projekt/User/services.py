from typing import Any 
from rich.console import Console
from rich.table import Table
from datetime import datetime
from .crud import UserCRUD

class UserService:
    def __init__(self, db: Any, user_crud: UserCRUD)->None:
        self.db = db
        self.user_crud = user_crud

    def add_user(self, user: Any) -> None:
        data = self.db.load_data()
        data["users"].append(user)
        self.db.save_data(data)

    def get_users(self) -> list:
        data = self.db.load_data()
        return data["users"]
    
    def get_user_borrow_history(self, user_id:int) -> None:
        console = Console() 
        user= self.user_crud.find_user_by_id(user_id)

        borrow_history = user.get('borrow_history', [])

        borrow_table = Table(title = "Historia wypożyczeń")
        borrow_table.add_column("Lp", justify="center")
        borrow_table.add_column("Book ID", justify="center")
        borrow_table.add_column("Data wypożyczenia", justify="center")

        if borrow_history:
            for i, event in enumerate(borrow_history, start = 1):
                try: 
                    book_id, iso_time = event
                    dt = datetime.fromisoformat(iso_time)
                    format_time = dt.strftime("%d-%m-%Y %H:%M")
                except:
                    book_id = event[0] if isinstance(event, list) and len(event) > 0 else "-"
                    format_time = iso_time if len(event) > 1 else "-"

                borrow_table.add_row(str(i), str(book_id), format_time)
        else:
            borrow_table.add_row("-", "Brak danych")

        console.print(borrow_table)
            
    def get_user_return_history(self, user_id:int) -> None:
        console = Console() 
        user= self.user_crud.find_user_by_id(user_id)

        return_history = user.get('return_history', [])

        return_table = Table(title = "Historia zwrotów")
        return_table.add_column("Lp", justify="center")
        return_table.add_column("Book ID", justify="center")
        return_table.add_column("Data zwrotu", justify="center")

        if return_history:
            for i, event in enumerate(return_history, start = 1):
                try: 
                    book_id, iso_time = event
                    dt = datetime.fromisoformat(iso_time)
                    format_time = dt.strftime("%d-%m-%Y %H:%M")
                except:
                    book_id = event[0] if isinstance(event, list) and len(event) > 0 else "-"
                    format_time = iso_time if len(event) > 1 else "-"

                return_table.add_row(str(i), str(book_id), format_time )

        else:
            return_table.add_row("-", "Brak danych")

        console.print(return_table)