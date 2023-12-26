# inheritance 

class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
    def introduction(self):
        return f'My name is {self.name} and im {self.age} years old'

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id=student_id
    
    def introduction(self):
        return f'My name is {self.name} and my student id number is {self.student_id}'

class Lecturer(Person):
    def __init__(self, name, age,lecture_id):
        super().__init__(name, age)
        self.lecture_id=lecture_id
    
    def introduction(self):
        return f'Its me your lecturer {self.name}'




object_person=Person('John Doe',28)
print(object_person.introduction())
std_watson=Student('Michael Watson',20,'STD256')
print(std_watson.introduction())
lect_jordan=Lecturer('Stuard Jordan',45,'LECT100')
print(lect_jordan.introduction())


