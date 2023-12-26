# try -> test a block of code for errors
# except -> let you handle the error
# else -> lets you execute code when there is no error
# finally ->lets you execute code, regardless of the result of try except

try:
    print('hello')
except:
    print('error occured')

try:
    print(xyz)
except:
    print('error occured')


# you can have many exceptions

try:
    print(hello)
except NameError:
    print('variable hello is not defined')
except:
    print('exception occured or there is a error in your program')


# else
try:
    print(test)
except:
    print('error')
else:
    print('there is no error in the program')


try:
    print('test')
except:
    print('error')
finally:
    print('code execution is finally completed')

# you can raise an exception in the program as a python developer, to raise the exception you can use raise keyword (raise Exception)

a=50
if a>40:
    raise Exception('numbers greater than 40 is not allowed')

test='hello'
if not type(test) is int:
    raise TypeError('only integers are allowed')


