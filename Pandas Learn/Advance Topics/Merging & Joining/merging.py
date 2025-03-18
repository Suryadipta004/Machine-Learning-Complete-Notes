import pandas as pd

# Creating the Customers DataFrame
df_Customers = pd.DataFrame({
    'CustomerId': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
})

# Creating the Orders DataFrame
df_orders = pd.DataFrame({
    'OrderId': [101, 102, 103, 104, 105, 106, 107],
    'CustomerId': [1, 2, 3, 1, 2, 4, 5],  # Mapping to CustomerId
    'Amount': [250, 150, 400, 300, 200, 500, 100]
})

print("Customers DataFrame:")
print(df_Customers)

print("\nOrders DataFrame:")
print(df_orders)

# Merging the DataFrames
# df_merged = pd.merge(df_Customers, df_orders, on='CustomerId' , how = 'right')
# print("\nMerged DataFrame with right join: \n" , df_merged)

df_cross_merged = pd.merge(df_Customers, df_orders, how = 'cross')
print("\nMerged DataFrame with left join: \n" , df_cross_merged)

