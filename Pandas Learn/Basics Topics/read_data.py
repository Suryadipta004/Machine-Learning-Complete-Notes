import pandas as pd

# read data into a sataframe from a csv file
df_csv = pd.read_csv("sales_data_sample.csv", encoding='latin1') # latin1 or utf-8
df_xlsx = pd.read_excel("SampleSuperstore.xlsx")
df_json = pd.read_json("sample_Data.json", encoding='utf-8')
#if data is used in cloud storage then use gcsfs

print(df_json)