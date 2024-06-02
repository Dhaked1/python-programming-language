choice = int(input('press-1 to convert in lowercase\n and press-2 to convert in uppercase'))
s = input('enter a string:')
if choice ==1:
    s1 = s.lower()
    print(s1)
elif(choice ==2):
    s1 = s.upper()
    print(s1)
else:
    print('you entered wrong choice')    
