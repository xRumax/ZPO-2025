def validate_data(func):
    def wrapper(self, *args, **kwargs):
        if not self.email or '@' not in self.email:
            return "Error: Email is incorrect"

        if not self.password or len(self.password) < 8:
            return "Error: Password is too short"
        return func(self, *args, **kwargs)
    return wrapper

class Form:
    def __init__(self, email:str, password:str) -> None:
        self.email = email
        self.password = password

    @validate_data
    def submit_form(self) -> str:
        return f"The form has been successfully sent"

def main():
    form = Form('dawid@123', '12345678')
    print(form.submit_form())

if __name__ == "__main__":
    main()
