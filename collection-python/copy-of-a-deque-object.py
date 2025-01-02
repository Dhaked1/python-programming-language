import collections
tup1 = (1,3,5,7,9)
dq1 = collections.deque(tup1)
dq2 = dq1.copy()
print("content of dq1:")
print(dq1)
print("dq1 id:")
print(id(dq1))
print("\n content dq2:")
print(dq2)
print("dq2 id:")
print(id(dq2))
print("\n checking the first element of dq1 and dq2 are shallow copies:")
print(id(dq1[0]))
print(id(dq2[0]))