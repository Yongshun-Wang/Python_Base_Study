class Student:
    def __init__(self, name,age,address,num):
        self.name = name
        self.age = age
        self.address = address
        self.num = num
        print(f"学生{num}信息录入完成,学生姓名:{self.name},年龄:{self.age},家庭住址:{address}")


for number in range(1,5):
    print(f"当前录入第{number}位学位信息,总共需要录入5位学生信息")
    student = Student(name = input("请输入学生姓名:"),age=input("请输入学生的年龄:"),address = input("请输入学生的住址:"),num=number)

