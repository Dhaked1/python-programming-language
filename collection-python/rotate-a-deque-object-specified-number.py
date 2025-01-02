import collections
#declare an empty deque object
dq_object = collections.deque()
#Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
dq_object.append(12)
print("Deque before rotation:")
print(dq_object)
#rotate  once in positive direction
dq_object.rotate()
print("\n Deque after 1 postive rotation:")
print(dq_object)
dq_object.rotate(2)#Rotate twice in positive direction
print("\n Deque after 2 positive rotation:")
print(dq_object)
dq_object.rotate(-2)
print("\n deque after 2 negative rotations:")
print(dq_object)