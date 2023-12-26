# range() -> it allows you to generate the list of integers
x=list(range(1,11))
print(x)

y=list(range(1,11,2))
print(y)

# enumerate : it is useful function to use with for loop

index_count=0
for letter in 'Hello':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1
# use above example with enumerate 
for i,letter in enumerate('Hello'):
    print('At index {} the letter is {}'.format(i,letter))

#zip() -> you can use zip() function to quickly create a list of tuples by zipping up together two list
list1=[1,2,3,4,5,6]
list2=['a','b','c','d','e']
result=list(zip(list1,list2))
print(result)

# max and min 
print(max([1,20,40,100,50,40]))
print(min([1,20,40,100,50,40]))

# random
from random import randint
x=randint(1,50)
print(x)

from random import shuffle
list2=['a','b','c','d','e']
shuffle(list2)
print(list2)
