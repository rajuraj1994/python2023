# lambda expression allow us to create 'anonymous' functions.This basically means we can quickly make ad-hoc function without needing to properly defined the function using def.
# The key difference from using def and lambda is lambda's body is a single expression,not a block of statement.

# def square(num):return num**2
square=lambda num:num**2

result=square(5)
print(result)


numbers=[1,2,3,4,5]

result=list(map(lambda num:num**2,numbers ))
print(result)

check=list(filter(lambda num:num%2==0,numbers))
print(check)
