# the map function allows you to "map" a function to an iterable object.That is to say you can quickly call the same function to every item in the iterable like list.

def square(num):
    return num**2

numbers=[1,2,3,4,5]
result=list(map(square,numbers))
print(result)

# define the function
def splicer(name):
    if len(name)%2==0:
        return name
    else:
        return name[0]


myname=['John','Cindy','Ram','Sita','Kelly']
result=list(map(splicer,myname))
print(result)

# if there is the even number of characters in a name then return fullname
# if there is the odd number of characters in a name then return only   first character of name