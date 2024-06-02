# append(), method
company = ["IBM","HCL","WIPRO"]
company.append("GOOGLE")
print(company)

# extend(),method
desktop = ["dell","hp"]
company.extend(desktop)# takes only list as argument company.extend("dell","hp") gives error
print(desktop)
print(company)
# len() method
r = len(company)
print(r)
#index() method
print(company.index("dell"))
#insert() method
company.insert(2,"apple")
print(company)
#count() method returns the numberof times that value appears
h = ["ibm","wipro","hcl","wipro","tata","wipro"]
print(h.count("wipro"))
#remove() method
h.remove("hcl")
print(h)
h.remove("wipro")
print(h)
# clear() method use to remove all element
h.clear()
print(h)
#pop() method
g =[2,3,4,8,0,1,5,6,7]
g.pop(3)
print(g)
#copy() method
i = g.copy()
print(i)
#reverse() method
g.reverse()
print(g)
#sort() method
g.sort(reverse = True)
print(g)
# del statement
del g[4]
print(g)
del g[1:3]
print(g)
#del g # for deleating all elements and the list object too
#print(g) gives error g is not define like that because g is ge deleted with objecct 

#accessing elements of nested list
n = [2,3,["hello","crazygirl"],6,7,[787,6566,56]]
print(n[2][0])
print(n[2:3][0])
print(n[2:3])
print(n[2:3][0][1])
print(n[2:3][0][1][4])
l = [1,2,3]
m = [3,4,5]
print(l+m)
