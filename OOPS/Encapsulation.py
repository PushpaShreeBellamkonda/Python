# Process of combining attributes and methods within the class
# for Data Protection
'''
1.public 
2.private    --only class methods and inside the class
3.protected  --inside the class and its subclass
'''
class A:
    def __init__(self,a,b):
        self.__a=a  #private
        self.__b=b  #private

    def show_data(self):
        print('a : ',self.__a)
        print('b : ',self.__b)

obj1=A(10,20)
obj1.show_data()


# print(obj1.__a)  will get error bcoz we cant use private variables outside the class
# print(obj1.__b)


class A:
    def __init__(self):
        self._a=10  #protected
        self._b=20  #protected

class B(A):
    def __init__(self):
        A.__init__(self)

    def show_data(self):
        print('a : ',self._a)
        print('b : ',self._b)

obj=B()
obj.show_data()