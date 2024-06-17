import numpy as np
arr = np.arange(6).reshape(2,3)
print(arr)
newarr = arr.reshape(-1)
print(newarr)