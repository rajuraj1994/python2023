# list -> contains more than one value in a variable,mutable and are in ordered

fruits=['apple','mango','papaya','cherry','grapes','kiwi']
print(fruits)
# length of the list
print(len(fruits))
print(type(fruits))

list1=list(('apple','mango','papaya','cherry'))
print(list1)

# access list
print(fruits[1])
print(fruits[1][0])
print(fruits[2][1])
#range
print(fruits[2:5])
print(fruits[2:])
print(fruits[:4])

# negative indexing
print(fruits[-1])
print(fruits[-4:-1])

# change item using index number
fruits[3]='pear'
print(fruits)

fruits=['apple','mango','papaya','cherry','grapes','kiwi']
fruits[2:4]=['guava','banana']
print(fruits)

newfruits=['apple','mango','papaya','cherry']
#append()
newfruits.append('banana')
print(newfruits)

#insert()
newfruits.insert(0,'kiwi')
print(newfruits)

x= ["apple","banana","cherry"]
y= ["mango","pineapple","papaya"]
x.extend(y)
print(x)

fruits=['apple','mango','papaya','cherry','grapes','papaya','kiwi']
# remove()
fruits.remove('papaya')
print(fruits)
fruits=['apple','mango','papaya','cherry','grapes','papaya','kiwi']
#pop()
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)

#clear()
list1=[1,2,3,4,5,20.5,'hello',True]
print(list1)
list1.clear()
print(list1)

# del
list2=[1,2,3,4,5,20.5,'hello',True]
del list2
# print(list2)

# sort
list3=['apple','papaya','mango','cherry']
list3.sort()
print(list3)

# sort(reverse=True) ->descending ordre
list3=['apple','papaya','mango','cherry']
list3.sort(reverse=True)
print(list3)

x=[1,100,20,60,50]
x.sort()
print(x)

#reverse()
list3=['apple','papaya','mango','cherry']
list3.reverse()
print(list3)


# tuple
test=('apple','papaya','mango','cherry','papaya')
print(test)
print(test.count('papaya'))
print(test.index('mango'))

list1=list(test)
print(list1)














