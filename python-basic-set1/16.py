#append items from inerrable to the end of the array
from array import*
arr = array('i',[1,3,4,2,5,7,9])
print("original array:" +str(arr))
arr.extend(arr)
print("extended array:" +str(arr))