

class User:
    def __init__(self, username:str, role:str = "Guest"):
        self.username = username
        self.role = role

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"
    

def admin_access(func):
    def wrapper(self, user:User, *args, **kwargs):
        if user.role == "Admin":
            return func(self, user, *args, **kwargs)
        else:
            return f"Access Denied! {user.username} is not an Admin"
    return wrapper

def moderator_access(func):
    def wrapper(self, user:User, *args, **kwargs):
        if user.role in ["Admin","Moderator"]:
            return func(self, user, *args, **kwargs)
        else:
            return f"Access Denied! {user.username} is not an Moderator"
    return wrapper

def guest_access(func):
    def wrapper(self, user:User, *args, **kwargs):
        return func(self, user, *args, **kwargs)
    return wrapper


class Program:
    @admin_access
    def delete_user(self, user:User):
        return f"User deleted by {user.username} | {user.role}."
    
    @moderator_access
    def edit_user(self, user:User):
        return f"User updated by {user.username} | {user.role}"
    
    @guest_access
    def get_user(self, user:User):
        return f"Get user by {user.username} | {user.role}"
    

def main():
    admin = User("David", "Admin")
    moderator = User("Marian", "Moderator")
    guest = User("Andrzej", "Guest")

    program = Program()
    print(program.delete_user(admin))
    print(program.get_user(guest))
    print(program.edit_user(moderator))
    print(program.get_user(admin))



if __name__ == "__main__":
    main()
