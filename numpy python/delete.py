import numpy as np
a = np.arange(1,11)
print("actual array is:",a)
b = np.delete(a,4)
print("modified array is",b)
x = np.array([[1,4,7,8],[9,11,3,2]])
c = np.delete(x,1,axis = 0)
print("actual array",x)
print("modified array",c)