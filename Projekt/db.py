import json
from pathlib import Path
from typing import Self

DB_PATH = Path("./Projekt/data.json")


class DatabaseSingleton:
    _instance = None

    def __new__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance

        return cls._instance

    def load_data(self) -> dict:
        if not DB_PATH.exists():
            raise FileNotFoundError(f"Database file not found at {DB_PATH}")
        with open(DB_PATH, "r", encoding='utf8') as file:
            return json.load(file)
        

    def save_data(self, data) -> None:
        with open(DB_PATH, "w", encoding='utf8') as file:
            json.dump(data, file, ensure_ascii= False, indent=4)
        
    