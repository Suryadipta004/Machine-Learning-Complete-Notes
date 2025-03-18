import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda","Jason","Annie", "Robert", "Alice"],
    "Age": [24, 13, 53, 33, 45, 32, 34, 25],
    "Salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    "Performance Score (Out of 100%)": [85, 90, 88, 85, 92, 95 , 90, 88]
}

df = pd.DataFrame(data)
print("Sample Dataframe:")
print(df)

print("Names (Single column return series)")
print(df["Name"])

print("Selecting multiple columns")
print(df[["Name","Salary"]])



