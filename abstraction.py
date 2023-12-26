# abstaraction is a concept in OOP that allows you to simplify complex system by breaking into smaller one. in python you can implement abstarction using abstract classes and abstract method.

# abstract class: a class that cannot be instantiated on its own and  it is a blueprint for other classes.

# abstract method: are the methods that are declared in an abstract class but have no implementation in the abastract class itself. subclass that inherit from the abstract class are required to provide concrete implementation for these abstract methods.

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius) :
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius

# x=Shape()

obj_circle=Circle(10)
print(obj_circle.area())

