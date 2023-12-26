# variable :  it is a container to store value
# Eg text='welcome',text=20
# While writing the variable name ,keywords used in python must be avoided,you must avoid special character except underscore(_),must avoid numeric value at the begining or start of the name 

test='welcome to python bootcamp'
print(test)
# to check the data type, use the function type()
print(type(test))
print(type(20))

test=20.6
print(test)

fruits=['mango','orange','pineapple','cherry']
print(fruits)
print(type(fruits))

fruits=('mango','orange','pineapple','cherry')
print(fruits)

result=True
print(result)

student={
    'firstName':'Ram',
    'lastName':'Shah',
    'age':25,
    'subjects':['python','django','rest api']
}
print(student)
print(type(student))

list1=[1,3,100,105,200,1,3,105,100]
print(list1)
demo=set(list1)
print(demo)

# type casting 
x='20'
print(type(x))
y=int(x)
print(type(y))

z=str(20)
print(type(z))













