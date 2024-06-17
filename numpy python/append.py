import numpy as np
a = np.arange(1,11)
print("Actual array:",a)
b = np.append(a,44)
print("modified array:",b)
c = np.append(a,(88,12))
print("array c:",c)