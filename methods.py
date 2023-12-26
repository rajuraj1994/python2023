# methods are the function defined inside the body of the class.

class Circle:
    pi=3.14

    # automatically envoked function for object
    def __init__(self,radius=2):
        self.radius=radius
        self.area=radius*radius*self.pi

    # resetting the radius
    def setRadius(self,newradius):
        self.radius=newradius
        self.area=newradius*newradius*self.pi
    
    def getCircumference(self):
        return 2*Circle.pi*self.radius



x=Circle()
print('The area is',x.area)

# calling the methods 
x.setRadius(10)
print('The new area is',x.area)
print('the new radius is',x.radius)

print('the circumference is',x.getCircumference())