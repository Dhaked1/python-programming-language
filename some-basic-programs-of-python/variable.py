x = 4
print(x)
x = "hello"
print(x)
x = y = z = 5
print(x,y,z)
x,y,z = 4,5,"hello"
print(y,x,z)
p,q,r = 5,10,7
q,p,r = p+1,r+2,q
print(p,q,r)
x = 8
print(type(x))
print(id(9))

#input from user
print("enter your name")
x = input()
print("hello"+x)#input() function alwayes take string as input
print(p,q,r,sep='$',end=' ')

