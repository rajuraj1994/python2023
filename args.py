# *args : when a function parameter starts with an asterisk,it allows for an  arbitary numbers of arguments and function takes them in as a tuple of values.

def demoFunction(*args):
    return sum(args)

result=demoFunction(10,20,30,40)
print(result)

