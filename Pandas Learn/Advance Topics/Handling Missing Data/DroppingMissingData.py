# Dropping missing data:
# dropna() drop rows or columns with missing data.

import pandas as pd
import numpy as np

data = {
    "Name": ["John", "Anna", np.nan , "Linda", "Jason", "Annie", "Robert", "Alice",
             "Michael", "Sarah", "David", "Sophia", "Daniel", "Emma", "James", "Olivia"],
    "Age": [24, 13, 53, 33, 45, 32, 34, 25, 41, 29, 50, 28, 36, 27, 40, 31],
    "Salary": [30000, 40000, 50000, 60000, 70000, np.nan, 90000, 100000,
               110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000],
    "Performance Score": [85, 90, 88, 85, 92, 95, 90, 88,
                                        91, 87, 89, 94, 86, 93, 88, 90],
    "Department": ["HR", "IT", np.nan, "Marketing", "Sales", "HR", "IT", "Finance",
                   "Marketing", "Sales", "HR", "IT", "Finance", "Marketing", "Sales", "HR"],
    "Years of Experience": [2, 1, 15, 7, 12, 5, 10, np.nan, 14, 6, 20, 4, 11, 8, 13, 9],
    "Location": ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston", "Seattle", "Miami", "Boston",
                 "Denver", "Austin", "Philadelphia", np.nan, "San Diego", "Atlanta", "Las Vegas", "Portland"]
}


df = pd.DataFrame(data)
print(df)

# df.dropna(inplace=True)
# print(df)

# df.dropna(axis = 1 , inplace=True)
# print(df)