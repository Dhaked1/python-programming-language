import numpy as np
a = np.array([1,2,3,2,4,5])
print("a:",a)
print(a[0],a[4])
print('\n')
a = np.array([[1,2,3,4],[5,4,3,2],[9,30,3,5]])
print("array:",a)
print(a[2,3])
print(a[2])#picking a row
print("\n")
x = np.arange(48).reshape(3,4,4)
print("array x:\n",x)
print(x[2])#picking a matrix
print(x[1,1,1:3])