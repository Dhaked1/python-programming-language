import numpy as np
arr = np.array([1,2,3])
print(arr)               
for x in arr:
    print(x)
#<---2D array----->
array = np.arange(6).reshape(2,3)
print(array)
for x in array:
    print(x)
#iterating through element
for x in array:
    for y in x:
        print(y)
#<---------3D array------------->
arr = np.array([[[1,2,3],[4,3,5]],[[6,8,7],[9,8,0]]])
for x in arr:
    print(x)
#element iteration
for x in arr:
    for y in x:
        for z in y:
            print(z)