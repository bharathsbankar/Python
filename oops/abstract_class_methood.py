from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def Process(self):
        return "hi"
        pass
    def add(self):
        pass
class Research(Student):
    def __str__(self):
        return "student"
    def Process(self):
        print(f"{self} is a researcher")
obj=Research()
obj.Process()