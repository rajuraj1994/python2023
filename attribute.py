# attribute -> characteristics or properties of an object

# defining the class
class Student:
    def __init__(self,full_name,age,gender):
        # defining the attribute
        self.name=full_name
        self.age=age
        self.batch='IT02'
        self.gender=gender


# instance of class 
obj_ram=Student(full_name='Ram Karki',age=25,gender='m')

# to access the attribute from the class do like this
print(obj_ram.name)
print(obj_ram.batch)

# to create another object 
obj_john=Student(full_name='John Doe',age=27,gender='m')
print(obj_john.name)


class Bird:
    def __init__(self,name,fly):
        self.name=name
        self.fly=fly

object_penguin=Bird(name='Penguin', fly='cannot fly')
print(object_penguin.name)
print(object_penguin.fly)
