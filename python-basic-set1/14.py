#get the current memory address and size of memory buffer in bytes
from array import*
a = array('i',[1,2,3,4,5,6])
print("original array:" +str(a))
print("current memory address and the lenght in elements of the buffer :" +str(a.buffer_info()))
print("The size of the memory buffer in bytes:" +str(a.buffer_info()[1]*a.itemsize))