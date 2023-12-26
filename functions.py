# function: a block of code to perform the certain task

# defining the task of function
def demo():
    print('Hello world')


# call (envoked) a function
demo()


# defining the function with parameters
def add(x,y):
    sum=x+y
    return sum



# call the function using arguments
a=int(input('enter the first value: '))
b=int(input('enter the second value: '))
data=add(a,b)
print(data)

# function with return type

def check(num):
    if num%2==0:
        return 'the number is even'
    else:
        return 'the number is odd'


# call the function 
result=check(10)
print(result)