var = True
while var:
    choice = int (input("Press-1 to find the ordinal value\n press -2 to find a character of a value \n"))
    if choice == 1:
        ch = input("enter a character:")
        print(ord(ch))
    elif choice ==2:
        val = int(input("enter a integer value:"))
        print(chr(val))
    else:
        print('you entered wrong choice')     
    print('do you want to continue?y|n\n')
    option = input()    
    if option =='y' or option =='Y':
        var = True
    else:
        var = False    

