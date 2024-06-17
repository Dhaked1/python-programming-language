import numpy as np
arr = np.array([1,2,3,4,6,2,3,1,8,0])
print(arr)
print(type(arr))
list = [1,3,5,2.5,6,0]
arr1 = np.array(list)
print(arr1)#if one element is float then all element will become float
print(type(arr1))
list1 = [1,3,2,"4",5,3]
arr2 = np.array(list1)
print(arr2)#if one element is string then all will become string
print(type(arr2))
list3 = [1,3,2,"4",5,3,4.5]
arr3  = np.array(list3)
print(arr3)#if one element is float and one is string then also all will be string not float
print(type(arr3))