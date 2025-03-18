# Filling by value:

# fillna() replaces NA values with non-NA data.
# Replace NA with a scalar value
import pandas as pd
import numpy as np
pd.set_option('future.no_silent_downcasting', True)# to avoid warning message in the console.

data = {
    "Name": ["John", "Anna", pd.NA, "Linda", "Jason", "Annie", pd.NA, "Alice",
             "Michael", "Sarah", "David", pd.NA, "Daniel", "Emma", "James", "Olivia"],
    "Age": [24, 13, 53, pd.NA, pd.NA, 32, 34, 25, 41, 29, 50, pd.NA, 36, 27, pd.NA, 31],
    "Salary": [30000, 40000, 50000, pd.NA, 70000, pd.NA, 90000, 100000,
               110000, 120000, pd.NA, 140000, 150000, pd.NA, 170000, 180000],
    "Performance Score": [85, pd.NA, 88, 85, 92, 95, 90, 88,
                          pd.NA, 87, 89, 94, 86, 93, 88, pd.NA],
    "Department": ["HR", "IT", pd.NA, "Marketing", pd.NA, "HR", "IT", "Finance",
                   "Marketing", "Sales", "HR", pd.NA, "Finance", "Marketing", "Sales", "HR"],
    "Years of Experience": [2, pd.NA, 15, 7, 12, pd.NA, 10, pd.NA, 14, 6, 20, 4, pd.NA, 8, 13, 9],
    "Location": ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston", pd.NA, "Miami", "Boston",
                 "Denver", pd.NA, "Philadelphia", pd.NA, "San Diego", "Atlanta", "Las Vegas", pd.NA]
}

df = pd.DataFrame(data)
print(df , "\n")

# print(df.fillna(0), "\n",)

# # Fill gaps forward or backward
# print(df.ffill(), "\n")
# print(df.bfill(), "\n")

# Limit the number of NA values filled

# print(df.ffill(limit=1), "\n") # limit=1 means only one missing value will be filled

# NA values can be replaced with corresponding value from a Series or DataFrame where the index and column aligns between the original object and the filled object.
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)
print(df.isna().sum())