from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def display(self, indent:int = 0) -> None:
        pass

class File(FileSystemComponent):
    def display(self, indent: int =0) -> str:
        return "  " * indent + f"- File: {self.name}"

class Directory(FileSystemComponent):
    def __init__(self, name:str) -> None:
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent = 0):
        result = "  " * indent + f"+ Directory: {self.name}"
        for child in self.children:
            result += "\n" + child.display(indent + 1)
        return result
    

def main():
    root = Directory("root")
    root.add(File("readme.txt"))
    root.add(File("data.csv"))

    src = Directory("src")
    src.add(File("main.py"))
    src.add(File("utils.py"))

    tests = Directory("tests")
    tests.add(File("test_main.py"))

    src.add(tests)
    root.add(src)

    print(root.display())


if __name__ == "__main__":
    main()
