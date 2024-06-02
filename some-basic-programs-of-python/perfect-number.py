num = int(input("enter a number:"))
sum =0
for i in range(1,num):
    if(num%i==0):
        sum = sum+i
if num ==sum:
    print('yes a perfect number') 
else:
    print('not a perfect number')
               





