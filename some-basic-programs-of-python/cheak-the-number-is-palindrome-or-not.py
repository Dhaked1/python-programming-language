num = int(input('enter a number:'))
res = 0
n = num
while num>0:
    rem = num%10
    res = rem+res*10
    num = num//10
if res == n:
    print('number is palindrome') 
else:
    print('number is not palindrome')








