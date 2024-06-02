num = input('enter a number')

l = len(num)
n = int(num)
sum = 0
num = n
while n>0:
    rem = n%10
    sum = sum+rem**l
    n = n//10
if num ==sum:
    print('it is a armstrong number')
else:
    print('not a armstrong number')






