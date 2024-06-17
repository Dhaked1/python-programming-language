import numpy as np
array1 = np.array([1,2,3,4,5,2,9,0],dtype=np.float32)
print(array1)
array1 = array1.astype(int)
print(array1)
array1 = array1.astype(str)
print(array1)
print(array1.shape)