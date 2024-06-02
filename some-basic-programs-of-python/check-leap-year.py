year = int(input('enter a year:'))
if year%100 == 0 and year%400==0:
    print('yes it is a leap year')
elif year%4 ==0:
    print('yes it is a leap year')
else:
    print('not a leap year')  


