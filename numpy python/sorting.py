#<--------------------using sort()--------------------------->
import numpy as np
x = np.array([1,4,2,378,5,6,9,90,78,11])
y = np.sort(x)#creats copy of sorted array
print("x = ",x)
print("y = ",y)
#<-----------using slicing operator------------->
y = np.sort(x)[::-1]#for decreasing order sorting
print("\n y = ",y)
#<---------------using argsort()------------------------------>
y = np.argsort(x)
print("\n sorted y:",y)#return the index position of sorted array 
#<----------ndarray.sort()----------------->
x.sort()
print("x = ",x)#doesn't creats copy use same memory only