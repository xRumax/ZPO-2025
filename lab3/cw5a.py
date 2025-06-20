from abc import ABC, abstractmethod
class Theme(ABC):
    def set_theme(self):
        pass 

class LightThemeRenderer(Theme):
    def set_theme(self) -> None:
        print("Light theme PDF")

class DarkThemeRenderer(Theme):
    def set_theme(self) -> None:
        print("Dark theme PDF")

class Document(ABC):
    def __init__(self, theme: Theme) -> None:
        self.theme = theme

    @abstractmethod
    def show_pdf(self):
        pass

class PDFDocument(Document):
    def show_pdf(self) -> None:
        self.theme.set_theme()       

def main():
    doc = PDFDocument(LightThemeRenderer())
    doc2 = PDFDocument(DarkThemeRenderer())

    doc.show_pdf()
    doc2.show_pdf()
    
if __name__ == "__main__":
    main()
