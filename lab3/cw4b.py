from abc import ABC, abstractmethod

class PermissionComponent(ABC):
    @abstractmethod
    def get_permissions(self):
        pass

    @abstractmethod
    def show(self):
        pass


class User(PermissionComponent):
    def __init__(self, name: str)->None:
        self.name = name
        self.permission = set()

    def add_permission(self, permission) -> None:
        self.permission.add(permission)

    def get_permissions(self):
        return self.permission
    
    def show(self)->str:
        return self.name
    
class Group(PermissionComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.permissions = set()
        self.members = []

    def add_member(self, member:PermissionComponent) -> None:
        self.members.append(member)

    def add_permission(self, permission) -> None:
        self.permissions.add(permission)

    def get_permissions(self):
        all_permissions = set(self.permissions)
        for member in self.members:
            all_permissions.update(member.get_permissions())
        return all_permissions
    
    def show(self) -> str:
        return self.name
    

def main():
    anna = User("Anna")
    anna.add_permission("read")

    marek = User("Marek")
    marek.add_permission("write")

    editors = Group("Editors")
    editors.add_member(anna)
    editors.add_permission("edit")

    admins = Group("Admins")
    admins.add_member(marek)
    admins.add_member(editors)
    admins.add_permission("delete")

    print(f"Uprawnienia grupy Admins: {admins.get_permissions()}")
    print(f"Uprawnienia użytkownika Anna: {anna.get_permissions()}")



if __name__ == "__main__":
    main()