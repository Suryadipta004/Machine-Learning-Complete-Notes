import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda","Jason","Annie", "Robert", "Alice"],
    "Age": [24, 13, 53, 33, 45, 32, 34, 25],
    "Salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    "Performance Score (Out of 100%)": [85, 90, 88, 85, 92, 95 , 90, 88]
}

df = pd.DataFrame(data)
# print(df)


high_salary = df[df["Salary"] > 50000]
print("Filtering rows based on single instructions: ")
print(high_salary)

print("\n")

filtered = df[(df["Age"] > 35) & (df["Salary"] >= 50000)]
print("Filtering rows based on Combined instructions: ")
print(filtered)

print("\n")

filtered_OR = df[(df["Age"] > 30) | (df["Performance Score (Out of 100%)"] < 90)]
print("Emplyees older than 35 OR performance score < 90 : ")
print(filtered_OR)