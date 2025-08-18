class person:
    pass
class Student(person):
    pass
class teachers(person):
    pass
class workers(person):
    pass

class personFactory:
    def get_person(self,p_type):
        if(p_type=='w'):
            return workers
        if(p_type=='s'):
            return Student
        if(p_type=='t'):
            return teachers 

pf=personFactory()

wk = pf.get_person('w')
st = pf.get_person('s')
tc = pf.get_person('t')