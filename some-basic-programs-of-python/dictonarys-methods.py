marks = {"physics":75,"chemistry":78,"maths":90}
for i in marks:
    print(i,":",marks[i])
#change and add values in dictionaries
marks["chemistry"] = 77
marks["english"] = 88
print(marks)   

#delete elements from a dictionary
#using del statement
del[marks["english"]]
print(marks)
#using pop() method
marks.pop("maths")
print(marks)
#cheak the existance of a key in a dictionary
l =  {"physics":75,"chemistry":78,"maths":90}
print('chemistry' in l)
print('english' in l)
print(78 in marks)
#search a value of dictionaries
print(75 in l.values())
#pretty printing
import json
print(json.dumps(l,indent = 2))





