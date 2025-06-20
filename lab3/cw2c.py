import time
from datetime import datetime


def request_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time

        log_entry = f"{datetime.now()} | {func.__name__} | Execution time : {duration:.6f} seconds \n"
        print(log_entry)
        return result
    return wrapper



class User:
    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        
    @request_time
    def insert_record(self, record) -> str:
            time.sleep(0.5) 
            return f"Record {record} inserted successfully"        


def main():
    user = User("Arek", "arek@123", "lmasl0")
    print(user.insert_record({"username" : user.username, "email": user.email, "password": user.password}))

if __name__ == "__main__":
    main()