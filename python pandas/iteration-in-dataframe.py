import pandas as pd
data = [[1005,1090],['A1','B1'],[23000,18000]]
D = pd.DataFrame(data)
print(D) 
print(D.shape,D.size)

for row in range(D.shape[0]):
    print("Row",row,"Columns",end=" ")
    for col in range(D.shape[1]):
        print(D[col][row],end=" ")
    print()