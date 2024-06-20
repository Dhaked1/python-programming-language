import pandas as pd
data = {'name':['ram','sita'],'marks':[19,23]}
D = pd.DataFrame(data,index=[1,2])
print(D)
D.to_csv("alka.csv")