# len() function
s = "i love my india"
print(len(s))
#find function
print(s.find("my",4,15))
print(s.find("my",8,15))
#isalnum() function returns true if characters in string is alphabets otherwise false
print(s.isalnum())#in s white space is there hence it returns false
a = "alka"
print(a.isalnum())
print('\n')
#is alpha() function
print(s.isalpha())
print(a.isalpha())
#isdigit() function
print('\n\n')
s = "dhakretgdv4566"
k =  "hgghfrffit5bhty"
q = "54468788553341"
print(s.isdigit())
print(k.isdigit())
print(q.isdigit())
print('\n')
#islower() function
print(s.islower())
q = "GVHEIRGJTHIY5UTY"
r = "ggfyghj"
print(q.islower())
print(r.islower())
print('\n')
#isupper() function
print(q.isupper())
p = "FGUHF"
print(p.isupper())
print('\n')
#isspace() function
p = "jay shree ram jay jay ram raja ram"
print(p.isspace())
print(" ".isspace())
h ='FGEHFHG'
#lower()
print(h.lower())
#upper()
q = "ram"
print(q.upper())
print(p.upper())
#lstrip()
s = "data structure"
print(s.lstrip("data"))
print(s.lstrip('dat'))
print(s.lstrip('at'))
print(s.lstrip('adt'))
print(s.lstrip('tad'))
#rstrip()
print(s.rstrip('eur'))
print(s.rstrip('ret'))
print(s.rstrip('tucers'))

#spli() function
print(s.split())



