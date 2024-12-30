#remove the first occurrence of a array
from array import*
array_num = array('i',[1,3,8,2,3,6,4,5,6])
print("original array:" + str(array_num))# (+) is used here for add two strings
print("remove the first occurrence of 3 from the array:")
array_num.remove(3)#insert the element which first occurrence you want remove
print("new array:"+str(array_num))