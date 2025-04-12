# we cant create obj to abstract class
# abstract method is a empty method
# abstract class==contains both abstract methods and normal methods

from abc import ABC,abstractmethod   #abc=abstract base class

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print('i have 3 sides')
class Rectangle(Polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print('i have 4 sides')

obj1=Triangle()
obj2=Rectangle()
obj1.no_of_sides()
obj2.no_of_sides()
