"""
vertically (row-wise) concatenation: pd.concat([df1, df2], axis=0 , ignore_index=True)
horizontally (column-wise) concatenation: pd.concat([df1, df2], axis=1 , ignore_index=True)

"""
import pandas as pd

# Creating the Customers DataFrame
df_Customers1 = pd.DataFrame({
    'CustomerId': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
})

df_Customers2 = pd.DataFrame({
    'CustomerId': [6, 7, 8, 9, 10],
    'Name': ['Jack', 'Ramu', 'Raj', 'Rahul', 'Ravi']
})

df_concat_ver = pd.concat([df_Customers1, df_Customers2], axis=0 , ignore_index=True)
print(df_concat_ver, "\n")


df_concat_hor = pd.concat([df_Customers1, df_Customers2], axis=1 , ignore_index=True)
print(df_concat_hor, "\n")
