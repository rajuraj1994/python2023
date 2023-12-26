# list comprehensions : it allows us to build out the list using a different notation.You can think of it as  essentially a one line for loop built inside of [] brackets.

for x in range(1,5):
    print(x**2)

result=[x**2 for x in range(1,11) ]
print(result)

# even numbers list 
check=[ x for x in range(1,20) if x%2==0]
print(check)

# convert celcius to fahrenheit
celcius=[0,10,20,1,32]
f=[((9/5)*temp+32) for temp in celcius]
print(f)
