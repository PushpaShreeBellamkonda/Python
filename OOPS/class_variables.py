'''
there are two tyes of variables inside a class
1)normal variables==which are accessed using self keyword
2)static variabls
'''

class Student:
    schl_name='xyz'        #static variable

    def __init__(self,id,name):
        self.id=id
        self.name=name
    def print_data(self):
        print(self.id,self.name)

Student1=Student(1,'pushpa')    #dynamic variable
Student2=Student(2,"shree")

Student1.print_data()
Student2.print_data()

print(Student1.schl_name)
print(Student2.schl_name)

Student.print_data(Student1)  #calling using class name
Student.print_data(Student2)


