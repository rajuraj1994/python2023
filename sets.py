#set: unorder collection of unique items
x={1,20,100,200,400,150,50,10,200}
print(x)

print(len(x))
print(type(x))

y=set(('a','b','c','d'))
print(y)

y.add('z')
print(y)

x.update(y)
print(x)

y.discard('b')
print(y)

y.pop()
print(y)

y.clear()
print(y)

a={1,2,3}
del a 
# print(a)

x={1,2,3,4,5,6}
y={5,6,7,3,8,9,10}
test=x.difference(y)
print(test)

test=x.intersection(y)
print(test)

