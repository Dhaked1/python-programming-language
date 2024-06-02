print(bool(0))
print(bool(45))
A = ["APPLE","banana","cherry"]
b = []
print(A,b)
#nested list
a = ["alka",6,8,[2,3,"dhaked"]]
print(a)
list = list(input("enter the elements:"))
print(list)
l1 = eval(input("enter the elements:"))
print(l1)
print(l1[0])
print(l1[2])

#traversing a list method1
day = list(input("enter elements"))
for i in day:
    print(i)

# traversing a list method 2
d = list(input("enter the element of list"))
for i in range(len(d)):
    print(d[i])

c = [1,12,'a']
print(c*3)

#slice operator
number = [12,34,53,3,5,67,8]
print(number[2:4])
print(number[-1:-7])
print(number[-7:-1])
# reverse the list
print(number[::-1])
# modification in list
number[2:4] = ["hello","alka"]
print(number)
# the value being assigned must be a sequence (list,tuple or string)
#number[2:3] = 78
#print(number)#TypeError:can only assign an iterable


