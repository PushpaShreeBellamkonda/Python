# class creation
class Student:
    def __init__(self,id,name,age):   #constructor
        self.id=id
        self.name=name
        self.age=age
    
    def easy(self):
        print(self.id,self.age,self.name)

# object creation
o1=Student(1,'stud1',18)
o2=Student(2,'stud2',18)

print(o1) #only prints the address of the object

print(o1.id,o1.age,o1.name)
print(o1.id,o1.age,o1.name)

# simple way
o1.easy()
o2.easy()

