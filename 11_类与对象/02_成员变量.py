class Student:
    name = None
    age = None
    def say_hi(self,msg):
        print(f"大家好我是{self.name},{msg}")

stu = Student()
stu.name = "王永顺"
stu.say_hi("我是你大爷")
