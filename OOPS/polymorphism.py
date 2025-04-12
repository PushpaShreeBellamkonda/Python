# 1.Method overloading

def add(a,b,c=0,d=0):
    return a+b+c+d

print(add(2,3))
print(add(2,3,4))
print(add(2,3,4,5))

# 2.Method Overriding

class Parent:
    def __init__(self):
        pass
    def height(self):
        print('height :',6.0)
    def education(self):
        print('education :','btech')
    def last_name(self):
        print('last name : ','Bellamkonda')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
    def height(self):
        print('height : ',5.10)
    def education(self):
        print('education : ','btech')

parent=Parent()
child=Child()
parent.height()
parent.education()
parent.last_name()
print('--------')
child.height()
child.education()
child.last_name()




class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f'{self.a} -- {self.b}'
    
obj=A(10,20)
print(obj)




