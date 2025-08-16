class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"<UNK>{self.age}<UNK>"
    def __lt__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.age == other.age

stu_1 = Student("wys",23)
stu_2 = Student("lsh",24)
print(str(stu_1))
print(stu_1>stu_2)
print(stu_1<stu_2)
print(stu_1==stu_2)
