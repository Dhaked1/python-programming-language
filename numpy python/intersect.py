import numpy as np
x = np.array(['keybord','bluetooth','printer','pendrive','mouse'])
y = np.array(['laptop','cpu','printer','mouse'])
print("intersection output:",np.intersect1d(x,y))
print("union of x,y is:",np.union1d(x,y))
print("elements that is present in x but not in y:",np.setdiff1d(x,y))
print("elements which are present in x also in y:",np.in1d(x,y))
print("elements which are present in y also in x",np.in1d(y,x))