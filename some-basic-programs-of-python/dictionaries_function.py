m = {"physics":54,"chemistry":44,'maths':66,'cs':65}
print(len(m))
m.clear()
print(m)
s = {"physics":54,"chemistry":44,'maths':66,'cs':65}
print(s.get("physics"))
print(s.items())

seq = s.items()
for i,j in seq:
    print(i,j)
print(s.keys())
print(s.values())
t = {'hindi':54,'chemistry': 88,'english':77}
s.update(t)
print(s)
