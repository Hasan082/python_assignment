class Person:
    def __init__(self, name, age) -> None:
        self.age = age
        self.name = name
        
    def introduce(self):
        return f"My name is {self.name} and my age is {self.age}"
        
        
class Student(Person):
    
    def __init__(self, name, age, course) -> None:
        super().__init__(name, age)
        self.course = course
        


obj = Student("John", 30, "Python")
obj1 = obj.introduce()
print(obj1)