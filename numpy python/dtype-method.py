#we can explicitly define the type of array element using dtype method
import numpy as np
list = [1,"2","3",5,7,3,0,56]
arr = np.array(list,dtype= float)
print(arr)
arr1 = np.array(list,dtype=int)
print(arr1)
list2 = [1,3.0,6.8,5,7,3,0,56]
arr2 = np.array(list2,dtype=str)
print(arr2)
arr2 = np.array(list2,dtype="U32")#for character data type uses Unicode32
print(arr2)