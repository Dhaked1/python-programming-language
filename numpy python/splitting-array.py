import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.split(arr,3)
print(newarr)
#<----split a 1D array to 4 part
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)
print(newarr)
#<------splitting 2D arrays------->
arr = np.array([[1,2],[3,4],[5,6],[7,3],[9,0],[22,4]])
newarr = np.array_split(arr,3)
print(newarr)
print("\n")
print(np.split(arr,2))
print('\n',np.vsplit(arr,2))
print('\n',np.hsplit(arr,2))