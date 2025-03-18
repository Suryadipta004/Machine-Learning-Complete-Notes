import pandas as pd

df_csv = pd.read_csv("sales_data_sample.csv", encoding='latin1') # latin1 or utf-8

print("Display the info the datafram \n")

print(df_csv.info()) # display the info of the dataframe