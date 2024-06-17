import numpy as np
array1 = np.arange(8)
print("original array:\n",array1)
#shape array with 2 rows and 4 columns
array2 = np.arange(8).reshape(2,4)
print("\n array reshaped with 2 rows and 4 columns:\n",array2)
array3 = np.arange(8).reshape(4,2)
print("reshaped array with 4 rows and 2 columns:\n",array3)
array4 = array1.reshape(2,2,2)
print("original array to reshaped 3D array:\n",array4)
a = np.arange(24).reshape(2,3,4)
print("\n",a)#plane = 2,column = 4
b = np.swapaxes(a,0,2)#plane change to column or viceversa
print("\n",b)#plane = 4 ,column =2

#<-----------------*-------------*--------------->
b = np.swapaxes(a,0,1)#before swapaxes plane 2 row 3
print(b)#now plane =3,rows  = 2