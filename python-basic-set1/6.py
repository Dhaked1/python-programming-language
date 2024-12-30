#insert an element
from array import*
array_num = array('i',[1,3,5,7,9])
print("original array:" +str(array_num))
print("insert new value 4 before 3:")
array_num.insert(1,4)
print("new array:"+str(array_num))