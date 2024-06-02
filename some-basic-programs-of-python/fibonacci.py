n = int(input('how many numbers you want in fibonacci series:'))
first = 0
second =1
i =3
print(first,second,end=" ")
while i<=n:
    third = first+second
    first = second
    second = third
    print(third,end='')
    i = i+1









