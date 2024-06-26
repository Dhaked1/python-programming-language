import numpy as np
a = np.arange(20).reshape(5,4)
b = np.arange(10,30).reshape(5,4)
print("matrix a:\n",a)
print("matrix b:\n",b)
print("maximum in a:\n",np.max(a))
print("sum of matrix a:\n",np.sum(a))
print("maximum element from each rows in matrix a\n",np.max(a,axis=1))
print("sum of all elements in each rows in matrix b",np.sum(b,axis=1))
print("mean of all term in each rows in matrix a\n",np.mean(a,axis=1))
print("mean of all terms in each column in matrix a\n",np.mean(a,axis=0))
print("median along row wise in matrix a:\n",np.median(a,axis=1))
print("median along column wise in matrix a :\n",np.median(a,axis=0))
print("standerd deviation along row wise in matrix a:",np.std(a,axis=1))