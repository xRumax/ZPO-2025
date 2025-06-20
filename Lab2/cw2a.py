from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def add_document(self) -> None:
        pass

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

class WordDocument(Document):
    def add_document(self) -> None:
        print("Adding Word document")

class PDFDocument(Document):
    def add_document(self) -> None:
        print("Adding PDF document")

class WordFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()

class PDFFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()
    
class Factory:
    _factories: dict
    def __init__(self)-> None:
        self._factories = {
            "PDF": PDFFactory,
            "Word": WordFactory,
        }
    
    def create_document(self, type_:str) -> Document:
        return self._factories[type_]().create_document()

def main():
    factory = Factory()
    word = factory.create_document("Word")
    pdf = factory.create_document("PDF")

    word.add_document()
    pdf.add_document()

if __name__ == "__main__":
    main()