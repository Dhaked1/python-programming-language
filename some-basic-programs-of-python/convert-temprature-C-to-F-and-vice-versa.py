a = int(input('press-1 for C to F\npress-2 for F to C\n:'))
if a==1:
    c = float(input('enter the temprature in degree celcius:'))
    f = (9/5)*c+32
    print(c,'celcius = ',f,"fahrenheit")
elif a==2:
    f = float(input('enter the temperature in fahrenheit:'))
    c = (f-32)*5/9
    print(f,'fahrenheit = ',c,'celcius')
else:
    print('you entered wrong choice')       


