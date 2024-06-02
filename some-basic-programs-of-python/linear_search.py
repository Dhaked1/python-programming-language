l = eval(input("enter the elements"))
key = eval(input("enter the element that you want to search:"))
for i in range(len(l)):
    if l[i] == key:
        print("element found at the position:",i+1)
        break
else:
    print("element not found")
