import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda", "Jason", "Annie", "Robert", "Alice",
             "Michael", "Sarah", "David", "Sophia", "Daniel", "Emma", "James", "Olivia"],
    "Age": [24, 13, 53, 33, 45, 32, 34, 25, 41, 29, 50, 28, 36, 27, 40, 31],
    "Salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
               110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000],
    "Performance Score": [85, 90, 88, 85, 92, 95, 90, 88,
                                        91, 87, 89, 94, 86, 93, 88, 90],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales", "HR", "IT", "Finance",
                   "Marketing", "Sales", "HR", "IT", "Finance", "Marketing", "Sales", "HR"],
    "Years of Experience": [2, 1, 15, 7, 12, 5, 10, 3, 14, 6, 20, 4, 11, 8, 13, 9],
    "Location": ["New York", "San Francisco", "Los Angeles", "Chicago", "Houston", "Seattle", "Miami", "Boston",
                 "Denver", "Austin", "Philadelphia", "Dallas", "San Diego", "Atlanta", "Las Vegas", "Portland"]
}


df = pd.DataFrame(data)
# print(df)

#square bracket df["column_name"] = some_Data
df["Bonus"] = df["Salary"] + df["Salary"] * 0.1
# print(df)

# use of insert() method
#df.insert(location , "Column Date" , some_data)
df.insert(0, "Employee ID", ["E01","E02","E03","E04","E05","E06","E07","E08","E09","E10","E11","E12","E13","E14","E15","E16"]) #(or) df.insert(0, "Employee ID", range(1, 17))
print(df)
