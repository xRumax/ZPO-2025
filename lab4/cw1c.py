from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, list: List):
        pass

class DESCSort(SortStrategy):
    def sort(self, data: List) -> List:
        return sorted(data, reverse=True)

class ASCSort(SortStrategy):
    def sort(self, data: List) -> List:
        return sorted(data)

class BubbleSort(SortStrategy):
    def sort(self, data: List) -> List:
        data = data.copy()
        for n in range(len(data) - 1,0,-1):
            swapped = False
            for i in range(n):
                if data[i] > data [i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    swapped = True
            if not swapped:
                break
        return data

class ChooseSort:
    def __init__(self, strategy: SortStrategy) -> None:
        self.strategy = strategy

    def choose_sort(self, data:List) -> List:
        return self.strategy.sort(data)

def main():
    arr = [3,4,5,6,1,2]
    desc = DESCSort()
    asc = ASCSort()
    bubble = BubbleSort()

    choose = ChooseSort(desc)
    sorted_list_desc = choose.choose_sort(arr)
    print(sorted_list_desc)

    choose2 = ChooseSort(asc)
    sorted_list_asc = choose2.choose_sort(arr)
    print(sorted_list_asc)

    choose3 = ChooseSort(bubble)
    sorted_list_bubble = choose3.choose_sort(arr)
    print(sorted_list_bubble)


if __name__ == "__main__":
    main()