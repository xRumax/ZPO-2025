from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    isbn: int
    name: str
    author: str
    year: int
    genre: str
    is_available: bool = True
    borrowed_by: int = None
    reservation_queue: Optional[list[str]] = []

