t1 = (1,2,3,4,5,6)
#method 1 of for loop
for i in t1:
    print(i)
#method 2 of for loopn
for i in range(0,len(t1)):
    print(t1[i])    
# method 3    
for i in range(len(t1)):
    print(t1[i])
t2 = (8,2,4,5,4,4)
print(t1+t2)
print(t1*2)
print(t1[1:6:2])
print(t1[::-1])#reverse a string
print(t1+(0,))
# max() function
p = max(t2)
print(p)
q = min(t2)
print(q)
print(t2.index(8))
print(t2.count(4))
#packing and unpacking in tuple
#packing
t = (2,5,7,0,9)
print(t)
#unpacking 
a,b,c,d,e = t
print(a)
print(b)
print(e)
#del(t)
#print(t) t is not defined is means tuple get deleted successfully





















