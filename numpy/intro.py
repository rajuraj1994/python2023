# numpy is a python library to work with arrays.numpy means numerical python.The array in numpy is called ndarray.

import numpy as np
nums=np.array([10,20,25,30])
print(nums)


# check the numpy version
print(np.__version__)
print(type(nums))

# dimension in array 
# 0-D Array 
test=np.array(10)
print(test)

# 1-D Array 
test=np.array([1,2,3,4])
print(test)

# 2-D array
test=np.array([[1,2,3],[4,5,6]])
print(test)

# 3-D array 
test=np.array([[[10,20,30],[15,25,35]],[[1,2,3],[4,5,6]]])
print(test)

