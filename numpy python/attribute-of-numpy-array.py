import numpy as np
array1 = np.array([1,2,3,6,4,5,0,8])
list1 = [[1,2,3],[8,54,9],[2,9,56]]
array2 = np.array(list1,dtype=float)
array3 = np.array([[[1,2,3],[4,6,5],[34,8,0],[23,6,8]]])
print(array1)
#<---------***dimensions of arrays***---------->
print("dimension of array1",array1.ndim)
print("dimension of array2",array2.ndim)
print("dimension of array3",array3.ndim)
#<--------------*shape of array*------------------>
print('shape of array1',array1.shape)
print("shape of array2",array2.shape)
print("array3",array3)
print("shape of array3",array3.shape)
#<--------------*size of array*--------------------->
print("size of array1",array1.size)
print("size of array2",array2.size)
print("size of array3",array3.size)
#<----------*datatype of arrays*-------------------->
print("datatype of array1",array1.dtype)
print("datatype of array2",array2.dtype)
print("datatype of array3",array3.dtype)
#<-----------*itemsize of arrays*------------>
print("iteamsize of array1",array1.itemsize)
print("iteamsize of array2",array2.itemsize)
print("iteamsize of array3",array3.itemsize)