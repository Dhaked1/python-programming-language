import numpy as np
print(np.ones((4,5),dtype = np.float32))
print(np.zeros((6,3),dtype = np.int8))
print(np.arange(1334,1339))
a = np.ones((2,3))
b = np.zeros((4,3))
print(np.concatenate([a,b]))
print('\n')
a = np.ones((4,1))
b = np.zeros((4,2))
print(np.concatenate([a,b],axis=1))
print(a.sum())#sum all entries
print(a.sum(axis=0))# sum over rows
print(a.sum(axis = 1))#sum over columns
print(a.sum(axis=1,keepdims= True))
print("\n")
array = np.random.random((5,6))
print(array)