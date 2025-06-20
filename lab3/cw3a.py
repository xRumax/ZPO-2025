import os
from typing import Any 

class FileCloseOpen:
    def open_file(self, filepath:str, mode:str ='r') -> Any:
        return open(filepath, mode)
    
    def close_file(self, file: Any) -> None:
        file.close()


class FileReader:
    def read_file(self, filepath: str, mode:str ='r') -> Any:
        if not os.path.exists(filepath):
            return FileExistsError(f"Error: {filepath} path doesnt exist")
        with open(filepath, mode) as file:
            return file.read()

class FileWriter:
    def write_file(self, filepath:str, content:str, mode:str ='a') -> Any:
        with open(filepath, mode) as file:
            file.write(content)

class FileDeleter:
    def delete_file(self,filepath:str) -> None:
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            print(f"Document {filepath} doesnt exist")


    
class DocumentFasade:
    def __init__(self, filepath)->None:
        self.filepath = filepath
        self.file_close_open = FileCloseOpen()
        self.file_reader = FileReader()
        self.file_writer = FileWriter()
        self.file_deleter = FileDeleter()
    
    def action(self,  action:str, *args) -> Any:
        if action == "Open":
            return self.file_close_open.open_file(self.filepath)
        elif action == "Close":
            file = args[0]
            return self.file_close_open.close_file(file)
        elif action == "Read":
            return self.file_reader.read_file(self.filepath)
        elif action == "Write":
            content = args[0]
            return self.file_writer.write_file(self.filepath, content)
        elif action =="Delete":
            return self.file_deleter.delete_file(self.filepath)
        else:
            return "Unsupported document action"
        
def main():
    document = DocumentFasade("test_3a.txt")
    print(document.action("Write", "abfafdasda"))
    file = document.action("Open")
    print(file.read())
    document.action("Close", file)
    #document.action("Delete")
    print(document.action("Read"))
if __name__ == "__main__":
    main()
