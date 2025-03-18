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

"""
df["Column Nmae"].mean()
df["Column Name"].median()
df["Column Name"].mode()
df["Column Name"].std()
df["Column Name"].var()
df["Column Name"].sum()
df["Column Name"].count()
df["Column Name"].min()
df["Column Name"].max()
"""
