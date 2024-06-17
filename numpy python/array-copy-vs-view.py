
#<-----------------copy------------->
import numpy as np
arr = np.array([1,2,3,4,56,7,])
x = arr.copy()
arr[0] = 43
print(arr)
print(x)
#<------------view------------------->
import numpy as np
arr = np.array([2,1,4,3,5,6])
x = arr.view()
arr[2] =23
print(arr)
print(x)