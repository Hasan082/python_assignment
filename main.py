class Person:
    school_name = "Notre Dame Collage, Dhaka"

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def intruduce(self):
        return "My name is {} and age is {} and I am a {}".format(self.name, self.age, self.gender)

    @classmethod
    def schoolNameMthod(cl):
        return cl.school_name

    @staticmethod
    def common():
        return "We are all from Rajabri, Dhaka"


obj1 = Person("John", 20, "Male")
obj2 = obj1.intruduce()
obj3 = Person.schoolNameMthod()
obj4 = Person.common()
findali_obj = "{} We everyine study at {} and Our home District is {}".format(
    obj2, obj1.schoolNameMthod(), obj1.common())
findali_obj = findali_obj.replace('\n', '')
print(findali_obj)
