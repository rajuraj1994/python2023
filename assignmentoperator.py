# assignment operator is used to assign value to a variable
# = means value assign 
# += eg:a+=b is same as a=a+b
# -= eg: a-=b is same as a=a-b
# *= eg : a*=b is sameas a=a*b
# **=, /=,//=,%=

x=20
y=10
x+=y
print(x)
x-=5
print(x)
x*=5
print(x)

y+=5
print(y)

# logical operator 
# and -> it will return true if all statemenet are true otherwise false 
# or -> it will return true if any one statement is true otherwise false
# not -> it gives the opposite result of the final reult

a=30
b=10
c=15
check= (a>b and b<c)
print(check)
check= a<b or b<c 
print(check)
print(not(check))


# 7%2 =1
# 3%2=1
# 1%2=1
# 0
# -> 0111

# 6%2=0
# 3%2=1

# membership operator 
fruits=['apple','mango','grapes','cherry']
print('mango' in fruits)
print('grapes' not in fruits)
print('a' not in fruits)

# identity operator 
a=['apple','mango']
b=['apple','mango']
c=a 
print(a is b)
# returns False because a is not a same object as b
print(a is c)
# return True

# arithmetic,comparison,logical,identity,membership,assignment and bitwise




