# dictionary: it always comes in key value pair, it is also known as object in other progrramming

student={
    'first_name':'John',
    'last_name':'Doe',
    'age':20,
    'gender':'male'
}
print(student)

print(student['first_name'],student['last_name'])

student=dict({'first_name':'John','last_name':'Doe'})
print(student)

student={
    'first_name':'John',
    'last_name':'Doe',
    'age':20,
    'gender':'male',
    'subjects':['python','django','REST API']
}
print(student['subjects'])
print(student['subjects'][0])

d={}
d['name']='Michael'
d['address']='NewYork'
print(d)

d['address']='Kathmandu'
print(d)

d.update({'address':'Paris'})
print(d)

d['email']='abc@example.com'
print(d)

d.pop('address')
print(d)

print(student.keys())

print(student.values())

print(student.items())

# nested dictionary
test={'key1':{'nestkey':{'subnestkey':'final result'}}}
print(test['key1'])
print(test['key1']['nestkey'])
print(test['key1']['nestkey']['subnestkey'])

# nested list : list inside aonther list
list1=[5,15,25,35]
list2=[10,20,30,40]
matrix=[list1,list2]
print(matrix)
print(matrix[1])
print(matrix[1][2])
print(matrix[0][1])
