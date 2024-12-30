#delete an element from array
from array import*
array_num = array('i',[1,2,3,4,5,6])
print("original array:" + str(array_num))# (+) is used here for add two strings
print("remove the third element from array:")
array_num.pop(2)# write the index whose index element you want to delete
print("new array:"+str(array_num))