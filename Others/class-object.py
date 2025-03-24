# class creation
class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

# object creation
o1=Student(1,'stud1',18)
o2=Student(2,'stud2',18)

print(o1) #only prints the address of the object

print(o1.id,o1.age,o1.name)