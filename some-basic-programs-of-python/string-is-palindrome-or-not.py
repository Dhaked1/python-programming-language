s=input('enter a string:')
length = len(s)
mid = length//2
revrr = -1
for i in range(mid):
    if s[i] == s[revrr]:
        i = i+1
        revrr = revrr-1
    else:
        print("not palindrome:")
        break
else:
    print("string is palindrome")            








