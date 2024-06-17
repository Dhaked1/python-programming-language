import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[3,9]]])
for x in np.nditer(arr):
    print(x)