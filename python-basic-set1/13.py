#get the length of array items in bytes
from array import*
a = array('i',[1,2,4,3,6,5,6,8])
print("original array:"+str(a))
print("length in bytes of one array items " +str(a.itemsize))