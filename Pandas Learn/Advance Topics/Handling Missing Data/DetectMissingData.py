# ?To detect these missing value, use the isna() or notna() methods.

import pandas as pd
import numpy as np

data = {
    "Name": ["John", "Anna", np.nan, "Linda", "Jason", "Annie", np.nan, "Alice",
             "Michael", "Sarah", "David", np.nan, "Daniel", "Emma", "James", "Olivia"],
    "Age": [24, 13, 53, np.nan, pd.NA, 32, 34, 25, 41, 29, 50, np.nan, 36, 27, np.nan, 31],
    "Salary": [30000, 40000, 50000, np.nan, 70000, np.nan, 90000, 100000,
               110000, 120000, np.nan, 140000, 150000, np.nan, 170000, 180000],
    "Performance Score": [85, np.nan, 88, 85, 92, 95, 90, 88,
                          np.nan, 87, 89, 94, 86, 93, 88, np.nan],
    "Department": ["HR", "IT", np.nan, "Marketing", np.nan, "HR", "IT", "Finance",
                   "Marketing", "Sales", "HR", np.nan, "Finance", "Marketing", "Sales", "HR"],
    "Years of Experience": [2, np.nan, 15, 7, 12, np.nan, 10, np.nan, 14, 6, 20, 4, np.nan, 8, 13, 9],
    "Location": ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston", np.nan, "Miami", "Boston",
                 "Denver", pd.NA, "Philadelphia", np.nan, "San Diego", "Atlanta", "Las Vegas", np.nan]
}


df = pd.DataFrame(data)
print(df)

print(df.isna().sum())

