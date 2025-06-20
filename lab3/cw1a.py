class System:
    def __init__(self, name:str) -> None:
        self.name = name

class Windows(System):
    def print_old(self) -> None:
        print(f"Printed Old system")

class Linux(System):
    def print_new(self) -> None:
        print(f'Printed New system')

class AdapterLinux:
    def __init__(self, windows: Windows) -> None:
        self.windows = windows

    def print_new(self) -> None:
        print("Printed New system")


def main():
    windows = Windows('Windows XP')
    linux = Linux('Ubuntu')

    windows.print_old()
    linux.print_new()
    adaptered_lin = AdapterLinux(windows)
    adaptered_lin.print_new()

if __name__ == "__main__":
    main()