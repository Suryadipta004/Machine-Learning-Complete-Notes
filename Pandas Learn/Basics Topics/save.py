import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Location": ["New York", "Paris", "Berlin", "London"],
    "Age": [24, 13, 53, 33],
    "City": ["Nagpur", "Kolkata", "Bihar", "Lucknow"]
}

df = pd.DataFrame(data) # create a dataframe from a dictionary
# print(df)

df.to_csv("created_files\data.csv" , index= False) # save the dataframe to a csv file
df.to_json("created_files\data.json" , index= False) # save the dataframe to a json file
df.to_excel("created_files\data.xlsx", index=False) # save the dataframe to an excel file
