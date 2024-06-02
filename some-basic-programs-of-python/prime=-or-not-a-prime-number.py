num = int(input('enter a number:'))
for i in range(2,num):
    if num%2==0:
        print('not a prime number')
        break
else:
    print("yes it is a prime number")



