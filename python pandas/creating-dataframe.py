import pandas as pd
employeeDB = {
    'id':[1001,10002,1003,1004,1005],
    'EMPName':['ramesh','danial','vikas','mahesh','rajendra'],
    'age':[30,31,32,33,45],
    'city':['bilaspur','raipur','durg','raigarh','agra']
}
EmpData = pd.DataFrame(employeeDB)
print(EmpData)
#<--------creating dataframe---------->
print('\n')
EmpData = pd.DataFrame(employeeDB,index=['A','B','E','F','E'])
print(EmpData)
#<----------creating dataframe using scalar value-------->
MyDict = {'name':'bunty','age':31}
emp1 = pd.DataFrame(MyDict,index=['A'])
print(emp1)
#<------***********--------->
MyDict1 = {'name':['bunty'],'age':43}
emp1 = pd.DataFrame(MyDict1)
print(emp1)