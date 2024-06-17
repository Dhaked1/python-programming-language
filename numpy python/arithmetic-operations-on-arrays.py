#<------------addition----------->
import numpy as np
list1 =[1,2,3,4,5,6]
list2 = [7,5,8,9,0,3]
arr1 = np.array(list1,dtype=int)
arr2 = np.array(list2,dtype=int)
print(arr1+arr2)
#<-----------*subtraction*--------------->
print(arr1-arr2)
#<--------*multiplication*------------>
a = np.array([[1,2],[3,4]])
b = np.array([[6,5],[11,45]])
print(a * b)#this (*) shows corresponding elements multiplication
print("\n")
print(a @ b)#this shows matrix multiplication
#<----------*simple division(*)----------->
list1 = [1,2,3,4,5,6,7,8,11]
list2 = [11,23,44,10,6,3,8,9,11]
array1 = np.array(list1)
array2 = np.array(list2)
array1.resize((3,3))
array2.resize((3,3))
simple_div = array2 / array1
print(simple_div)
#floor division//
c = array2//array1
print(c)
#<--------------exponentiation------------------->
c = array1**array2
print(c)

#<------------modulo--------------------->
c = array1%array2
print(c)
#<-----------transpose----------->
print("\n",array1)
print("\n",array2)
print("transpose of array1 is \n:",array1.transpose())
print("transpose of array2 is \n:",array2.transpose())