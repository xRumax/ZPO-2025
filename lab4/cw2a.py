from typing import Self, List
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
    

def main():
    arr = [1,2,3,4]

    it = Iterator(arr)


    for i in it:
        print(i)
    

if __name__ == "__main__":
    main()