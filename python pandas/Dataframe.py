import pandas as pd

data = [
    (1, 'vikas', 31, 'male', 'rachi'),
    (92, 'alka', 19, 'female', 'agra'),
    (3, 'varun', 20, 'male', 'patna'),
    (4, 'amit', 25, 'male', 'jaipur'),
    (5, 'ram', 12, 'male', 'avadh'),
    (6, 'sita', 23, 'female', 'janak')
]

df = pd.DataFrame(data, columns=['rollno', 'name', 'age', 'gender', 'address'])

# Print entire DataFrame
print("DataFrame:")
print(df)

# Print first few rows (head)
print("\nFirst few rows (head):")
print(df.head())

# Print last few rows (tail)
print("\nLast few rows (tail):")
print(df.tail())

# Print shape (number of rows, number of columns)
print("\nShape of DataFrame:")
print(df.shape)

# Print specific columns
print("\nAge column:")
print(df['age'])

print("\nAge and Name columns:")
print(df[['age', 'name']])

# Print number of elements (rows * columns)
print("\nNumber of elements in DataFrame:")
print(df.size)

# Print data types of columns
print("\nData types of columns:")
print(df.dtypes)

# Print values (numpy representation of DataFrame)
print("\nValues in DataFrame:")
print(df.values)

# Print index (row labels)
print("\nIndex of DataFrame:")
print(df.index)
print("\n")
print(df.age)
print(df.loc[0])
print(df.loc[4])
print(df.loc[[0,2,3]])
print(df.loc[0:3])#select multiplerows by range
print(df.iloc[0:3])#select multiplerows by iloc()
#filtering rows
print("\n")
print(df[df['age']>20])
print(df[df['name']=='ram'])
print('\n')
#adding new columns to dataframe
df['branchcode'] = 22
print(df.head)
print('\n')
#adding new column to dataframe in a particular location
df.insert(3,'mobilenumber',[10,20,30,31,29,56])
print(df.head())
print('\n')
#deleting a column
df = df.drop(columns=['mobilenumber'])
print(df.head(5))
del df['address']
print(df.head())