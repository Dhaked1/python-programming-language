def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input('enter a number to find factorial:'))
if num<0:
    print('sorry! factorial of negative numbers does not exist')
elif num ==0:
    print('factorial of zero is equal to 1')
else:
    print('factorial = ',factorial(num)) 
