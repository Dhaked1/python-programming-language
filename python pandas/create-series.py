import pandas as pd
s = pd.Series(['ind','aus','russ','japan','nz'])
print("\n",type(s))
print("\n",len(s))
print("\n",s)
#<------defining own index--------->
s = pd.Series(['ind','aus','russ','japan','nz'],index=["a","b","c","d","e"])
print("\n",s)
#<-----------another method to creat a series------------>
country = ['ind','aus','russ','japan','nz']
cost = [1000,2000,3000,4000,50000]
sales = pd.Series(cost,index= country)
#<---------creating series from tuple---------->
country = ('ind','aus','russ','japan','nz')
sales = (5000,4000,3000,1000,2000)
s = pd.Series(sales, index=country)
print("\n:",s)
#<-----------creating series using dictionary---------->
data = {"ind":9000,"aus":5000,"nz":3000}
print(pd.Series(data))