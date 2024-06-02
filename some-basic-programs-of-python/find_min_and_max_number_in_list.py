l = eval(input("Enter the elements :"))
#l = list(input("enter the elements"))
max = l[0]
min = l[0]
for i in range(len(l)):
    if min>l[i]:
        min = l[i]
    if max<l[i]:
        max = l[i]    
print("the minimum number in the list is :",min)
print("the maximum number in the list is:",max)

