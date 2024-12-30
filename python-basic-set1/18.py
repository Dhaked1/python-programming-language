# write a program to append item from a specified list
from array import*
num_list = [1,2,6,-8]
array_num = array('i',[])
print("items in the array list:"+str(num_list))
print("append items from the list:")
array_num.fromlist(num_list)
print("Items in the array :"+str(array_num))