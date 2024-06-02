print("what operand do you want")
operator = input("enetr either +,-,* or / ")
n1 = float(input("enter first number"))
n2 = float(input("enter second number"))
if operator == '+':
    print(n1+n2)
elif operator == '-':
    print(n1 - n2)
elif operator == '*':
    print(n1*n2)
elif operator == '/':
    print(n1/n2)
else:
    print("invalid operator entered")



