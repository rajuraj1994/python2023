# **kwargs: Its builds a dictionary of key value pairs

def demoFunction(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favourite fruit is {kwargs['fruit']}")
    else:
        print('not a favourite fruit')
# print('my fa',kwargs['fruit'])

demoFunction(fruit='apple')