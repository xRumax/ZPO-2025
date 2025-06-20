from abc import ABC, abstractmethod

class DocumentProcessor(ABC):
    name:str

    def __init__(self, name:str) -> None:
        self.name = name

    def run(self) -> None:
        self.open()
        self.analyze()
        self.classify()
        self.close()

    @abstractmethod
    def open(self) -> None:
        pass


    @abstractmethod
    def analyze(self) -> None:
        pass

    @abstractmethod
    def classify(self) -> None:
        pass

    def close(self) -> None:
        print("Document has been closed.")



class PDFDocument(DocumentProcessor):
    def open(self) -> None:
        print("PDF document has been opened.")

    def analyze(self) -> None:
        print("Analyzing PDF document...")

    def classify(self) -> None:
        print("PDF documnet has been classified to the Sport category.")

        

class DOCXDocument(DocumentProcessor):
    def open(self) -> None:
        print("DOCX document has been opened.")

    def analyze(self) -> None:
        print("Analyzing DOCX document...")

    def classify(self) -> None:
        print("DOCX documnet has been classified to the Sport category.")

        
        

def main():
    pdf_doc = PDFDocument("PDF")
    docx_doc = DOCXDocument("DOCX")

    pdf_doc.run()
    processors = [PDFDocument("PDF"),
                  DOCXDocument('DOCX')]
    
    for i in processors:
        i.run()

if __name__ == "__main__":
    main()