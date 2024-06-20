import pandas as pd
data = [[20,30],[60,40]]
D = pd.DataFrame(data,columns=['col1','col2'],index=['row1','row2'])
print(D)