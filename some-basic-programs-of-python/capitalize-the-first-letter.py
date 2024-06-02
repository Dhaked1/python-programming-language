s1=input("enter a string:")
a = 0
length = len(s1)
end = length
s2 = "" #empty string
while a<length:
    if a ==0:
        s2 = s2+s1[0].upper()
        a+=1
    elif(s1[a] == ' 'and s1[a+1]!=''):
        s2 = s2+s1[a]
        s2 = s2+s1[a+1].upper()
        a+=2
    else:
        s2 = s2+s1[a]
        a+=1
print("original string:",s1)
print("capitalized words string:",s2)

    
