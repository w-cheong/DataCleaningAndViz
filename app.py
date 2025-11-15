import pandas as pd
import csv
import logging

# Load raw data
FILE_PATH = 'https://raw.githubusercontent.com/gchandra10/filestorage/refs/heads/main/stock_market.csv'
df = pd.read_csv(FILE_PATH)

# inspect shape
print(df.shape)

#preview starting rows
print(df.head())

# convert headers to snake_case
def dataframe_cleaning(df):
    headers = df.columns.values
    print(headers)
    for new_name in headers:
        orig_name = new_name
        new_name = new_name.strip().replace(' ', '_') #stripped in case, then remove spaces with underscore
        df = df.rename(columns={orig_name: new_name})
        df[new_name] = df[new_name].str.strip() #strips whitespace from entire column
    print(df.head())

dataframe_cleaning(df)

# TODO: cleaned parquet
# df.to_parquet('cleaned.parquet')

# TODO: Aggregations
# df.to_parquet('agg1.parquet')
# df.to_parquet('agg2.parquet')
# df.to_parquet('agg3.parquet')