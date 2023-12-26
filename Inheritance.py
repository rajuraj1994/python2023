# inheritance is to form a new classes from the classes that have been already defined.The newly formed class  are called derived class and the class that we derive from are called base class.The derive class override or extend the functionality  of base class.

class Animal:
    def __init__(self):
        print('Animal class is created')
    
    def intro(self):
        print('Animal')
    
    def eat(self):
        print('Animal who eats')

class Dog(Animal):
    def intro(self):
        print('The animal type is Dog')
    
    def speak(self):
        print('Dog barks')
    


a=Animal()
print(a)
a.intro()
a.eat()
d=Dog()
d.intro()
d.eat()
d.speak()

