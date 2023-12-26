a=10
b=20
if a<b:
    print('a is less than b')
else:
    print('a is greater than b')

x=int(input('Enter the number: '))
if x%2==0:
    print(x,'is an even number')
else:
    print(x,'is an odd number')
    
# wap to check whether a number is divisible by 5 or not

x=20
y=10
z=15

if x>y and x>z:
    print('x is greater than y and z')
elif y>x and y>z:
    print('y is greater than x and z')
else:
    print('z is greater than x and y')

# leap lear 
year=int(input('please enter any year with century'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'is a leap year')
#    2000 -> t and f ->f or t ->t
else:
    print(year,'is not a leap year')
    







