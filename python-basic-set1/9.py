#convert ordinary array to list
from array import*
array_num = array('i',[1,2,3,4,5,6])
print("original array:" + str(array_num))# (+) is used here for add two strings
print("convert ordinary array to list:")
num_list = array_num.tolist()
print("list:")
print(num_list)