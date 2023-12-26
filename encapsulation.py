# it is a method that describes the concept of bundling data and methods within a single unit.Using encapsulation allow us to restrict accessing variables and methods directly and prevent accidental modification.

# access modifier : we can achieve encapaulation using access modifier
# public member: accessible anywhere from outside he class ege: self.name
# private member : accessible within the class eg: self.__salary
# protected member : acessible within the class and its child class eg:    self._project

class Company:
    def __init__(self):
        #protected member
        self._project= 'Machine Learning'

class Employee(Company):
    # constructor
    def __init__(self,name,salary):
        # public data memeber 
        self.name=name 
        # private data member
        self.__salary=salary
        Company.__init__(self)

    # public instance method
    def show(self):
        print('Name: ',self.name,'Salary: ',self.__salary)


emp=Employee('Ram',20000)
# print(emp.__salary)
emp.show()

# name mangling to access private members
#_classname__datamember 
print('Salary : ',emp._Employee__salary)

# access protected data member 
print(emp._project)

