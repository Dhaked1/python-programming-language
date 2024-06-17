import numpy as np
array = np.arange(20,40,2)
print("its original array:",array)
print("after boolean indexing:",array[array>25])
a = np.array([1,2,3,4,0,6])
print(a>3)
print(a+3)
print(a%2==0)
b = [True,False,True,True,False,True]
print(a[b])
arr = a.reshape(2,3)
print(arr)
print("\n")
b = [True,True,False,True,True,False]
print(a[b])