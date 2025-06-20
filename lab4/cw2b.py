from typing import List, Self

class Iterator:
    arr : List
    index:int
    add :int

    def __init__(self, arr: List) -> None:
        self.arr = arr[::-1]
        self.index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.index < len(self.arr):
            value = self.arr[self.index]
            self.index += 1
            return value        
        raise StopIteration