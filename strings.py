x="Welcome to python bootcamp"
print(x)

test="""This is the
multiline string in the 
python
"""
print(test)
# len() -> length of the string
print(len(x))

# index
print(x[0])
print(x[20])
print(test[0])

# slicing
print(x[3:6])
print(x[10:20])
# leaving out the end index
print(x[4:])
# leaving out the starting index
print(x[:10])

# negative indexing
print(x[-1])
print(x[-2])

# slicing using negative index
print(x[-6:-1])

print(x[:])

# upper
print(x.upper())

#lower
print(x.lower())

#strip
test="   welcome you    "
print(test)
print(test.strip())

# replace
y="Hello World"
print(y.replace('World','People'))

#split -> it will split the the text between specified character like comm(,) or whitespace or any charcters and it always return the value in the list format
print(x.split())
print(x.split('to'))

# concatenation (+)
a='Hello'
b='World'
c=a+" "+b
print(c)

age=25
# d="my current age is "+age
# print(d)
d="my current age is {}"
# {} -> placeholder
print(d.format(age))
print('my current age is',age)

quantity=5
itemno=230
a='i want to buy {} quantity of item no {}'
print(a.format(quantity,itemno))
test='i want to buy {0} quantity of item no {1}'
print(test.format(quantity,itemno))

# Escape Character
z="he said \"dont worry about it\""
print(z)

a='she typed \n"Hello World"'
print(a)














