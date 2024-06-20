import pandas as pd
data = [{'b':2,'c':3},{'a':10,'b':20,'c':30}]
df = pd.DataFrame(data,index=['first','second'])
print(df)