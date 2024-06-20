import pandas  as pd
df = pd.DataFrame()
print(type(df))
print(df)
#<----------creating empty dataframe(inserting columns)----------->
columndata = ['id','empname','age','city']
df = pd.DataFrame(columns=columndata)
print(df)
#<---inserting row(values) in empty dataframe--->
row1 = {'id':1001,"EMpname":"mahesh",'age':45,"city":"agra"}
df = df._append(row1,ignore_index = True)
df = df._append({'id':1002,'EMPname':'vikas','age':48,'city':'bilaspur'},ignore_index = True)
print(df)
#<---creating dataframe frome list--->
df2 = pd.DataFrame()
print("\n")
print(df2)#empty dataframe df2
df2['id'] = [1,2,3,4,5]
df2['emp2'] = ['A','B','C','D','E']
df2['salary'] = [1000,2000,3000,4000,5000]
df2['exp']=[1,2,3,4,5]
print('\n')
print(df2)