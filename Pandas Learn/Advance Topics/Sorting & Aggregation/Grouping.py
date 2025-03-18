import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'ID': np.arange(1, 21),  # IDs from 1 to 100
    'Name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Jack' , 'Ramu'], 20),
    'Age': np.random.randint(18, 60, 20),  # Random ages between 18 and 60
    'Salary': np.random.randint(30000, 120000, 20),  # Random salary between 30k and 120k
    'Department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing', 'Sales'], 20),
    'Performance_Score': np.random.uniform(1, 10, 20)  # Performance scores between 1 and 10
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())

"""
df.groupby("Age") groups the DataFrame by the "Age" column.
["Salary"] selects the "Salary" column from the grouped data.
.sum() computes the total salary for each age group.
"""

print(df.groupby(["Department","Name"])["Salary"].sum())

""""
df.groupby(["Department", "Name"]): Groups the DataFrame by both "Department" and "Name".
["Salary"]: Selects the "Salary" column.
.mean(): Computes the average salary for each (Department, Name) combination."
"""
