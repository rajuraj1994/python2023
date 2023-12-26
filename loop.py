# for loop : iteration
list1=[10,20,30,40,50]
for x in list1:
    print(x,end=' ')
print('\n')
text='hello world'
for y in text:
    print(y,end=' ')
print('\n')
for a in range(2,8):
    print(a,end=' ')
print('\n')
for a in range(5):
    print(a,end=" ")

print('\n')
for b in range(10,101,10):
    print(b,end=' ')
else:
    print('\n')
    print('completed')

# break 
fruits=['apple','mango','banana','papaya','grapes']
for i in fruits:
    if i=='banana':
        break
    print(i)

# continue
numbers=[1,2,3,4,5,6,7]
for j in numbers:
    if j==4:
        continue
    print(j)

for x in range(21):
    if x%2==0:
        print(x)
        