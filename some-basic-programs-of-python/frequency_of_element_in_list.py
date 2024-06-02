import json
s = input("enter a string:")
l = s.split()
d = {}
for w in l:
    key = w
    if key not in d:
        count = l.count(key)
        d[key] = count

print("the frequency of element in the list is as follows:")
print(json.dumps(d,indent = 2))





