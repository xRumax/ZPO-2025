class Person:
    def introduce(self) -> str:
        return "I'm a person"
    

class Worker(Person):
    def introduce(self) -> str:
        return "I'm a worker"


class Student(Person):
    def introduce(self) -> str:
        return "I'm a student"
    
class WorkingStudent(Worker, Student):
    pass
    

def main():
    person = Person()
    worker = Worker()
    student = Student()
    workingstudent = WorkingStudent()

    print(person.introduce())
    print(worker.introduce())
    print(student.introduce())
    print(workingstudent.introduce())


if __name__ == '__main__':
    main()