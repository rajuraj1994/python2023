# polymorphism -> means many forms of same methods and they behave differently in different classes.

class Bird:
    def intro(self):
        print('there are many types of birds')
    
    def fly(self):
        print('most of the birds can fly but some cannot')

class Parrot(Bird):
    def fly(self):
        print('Parrot can fly')

class Penguin(Bird):
    def fly(self):
        print('Penguin cannot fly')

    
obj_bird=Bird()
obj_bird.intro()
obj_bird.fly()

obj_parrot=Parrot()
obj_parrot.intro()
obj_parrot.fly()
obj_penguin=Penguin()
obj_penguin.intro()
