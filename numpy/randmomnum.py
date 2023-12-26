from numpy import random
num=random.randint(200)
print(num)

# random float 
num=random.rand()
print(num)

# 1-D array using random 
nums=random.randint(50,size=(4))
print(nums)

# 2-D array using random
nums=random.randint(100,size=(2,3))
print(nums)

# 1-D array float
a=random.rand(4)
print(a)

# 2-D array float
a=random.rand(3,4)
print(a)

# random data distribution 
# The sum of probability numbers should be 1

a=random.choice([2,4,6,8],p=[0.3,0.5,0.2,0],size=(20))
print(a)

a=random.choice([2,4,6,8],p=[0.3,0.5,0.2,0],size=(3,4))
print(a)