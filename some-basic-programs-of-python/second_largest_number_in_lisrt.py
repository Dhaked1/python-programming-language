l = eval(input("entr the elements of list:"))
second = max = l[0]
for i in range(len(l)):
    if max<l[i]>second:
        second = l[i]
print("the second largest number in a list is :",second)

