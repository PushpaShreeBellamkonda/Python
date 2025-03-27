class A:
    def __init__(self,a):
        self.a=a
    
    def print_a(self):
        print("a is :",self.a)

class B(A):    #A is parent,B is child class
    def __init__(self,a,b):
        A.__init__(self,a)
        self.b=b

    def print_b(self):
        print("b is : ",self.b)

obj1=B(10,20)
obj1.print_a() #without creating obj for class A we can access class A variables,bcoz in class B we have inherited class A
obj1.print_b()


# dialy life example

class Driver:
    def __init__(self,f_name,l_name,mbl,age):
        self.f_name=f_name
        self.l_name=l_name
        self.mbl=mbl
        self.age=age

    def full_name(self):
        return f'{self.f_name} {self.l_name}'
    

class Licence(Driver):
    def __init__(self,f_name,l_name,mbl,age,licence_id,validity):
        Driver.__init__(self,f_name,l_name,mbl,age)
        self.licence_id=licence_id
        self.validity=validity

    def is_valid_licence(self):
        if self.validity >= 2021:
            return True
        else:
            return False

user1_licence=Licence('a','b',234,21,111,2020)
print(user1_licence.full_name())
print(user1_licence.is_valid_licence())


