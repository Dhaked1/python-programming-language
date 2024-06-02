marks = {"physics":75,"chemistry":78,"maths":100}
print(marks)
d = {}
print(d)
#d1 = {[2,3]:"hello"}
#print(d1) error unhashable type:'list
#creating list using dict() constructor
m = dict(physics = 44,maths = 40,chemistry = 30)
print(m)
r = dict({"physics":75,"chemistry":78,"maths":100})
print(r)
# dict() constructor with zip() function
z = dict(zip(("physics","chemistry","maths","cs"),(23,34,56,34)))
print(z)
#dict() constructor using key-value pairs separately
m = dict([['physics',54],['chemistry',57],['maths',90]])
print(m)
a = dict((('physics',33),('chemistry',22),('maths',44)))
print(a)
# accessing value using key
print(a['maths'])
print(a.keys())#to access all keys in one go
print(a.values())#to access all values in one go
