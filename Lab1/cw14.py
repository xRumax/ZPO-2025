class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a+b
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a*b
    
    @classmethod
    def identify_matrix(cls, size: int) -> list[list[int]]:
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def main():
    for row in MathOperations.identify_matrix(3):
        print(row)


if __name__ == '__main__':
    main()