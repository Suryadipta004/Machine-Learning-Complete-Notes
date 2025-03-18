#head() , tail() methods are used to display the first and last n rows of the dataframe respectively.
import pandas as pd
df_csv = pd.read_csv("sales_data_sample.csv", encoding='latin1') # latin1 or utf-8

print("Display the first 10 rows of the dataframe \n")
print(df_csv.head(10))

print("Display the last 10 rows of the dataframe \n")
print(df_csv.tail(10))

