import pandas as pd

# convert headers to snake_case
def dataframe_cleaning(df):
    headers = df.columns.values
    print(headers)
    for new_name in headers:
        orig_name = new_name
        new_name = new_name.strip().replace(' ', '_') #stripped in case, then remove spaces with underscore
        df = df.rename(columns={orig_name: new_name})
        df[new_name] = df[new_name].str.strip() #strips whitespace from entire column
    return(df)
    
def main():
    # Load raw data
    FILE_PATH = 'https://raw.githubusercontent.com/gchandra10/filestorage/refs/heads/main/stock_market.csv'
    df = pd.read_csv(FILE_PATH)
    print(df.dtypes)

    # inspect shape
    print(df.shape)

    #preview starting rows
    print(df.head())

    #quick summary
    print(df.describe())

    df = dataframe_cleaning(df)

    #standardize text case for Validated
    validated_mapping = {'N': 'No', 'NO' : 'No', 'No': 'No', 'Y': 'Yes', 'YES': 'Yes', 'Yes': 'Yes', 'n': 'No','y': 'Yes'}
    df['Validated'] = df['Validated'].map(validated_mapping, na_action='ignore').fillna('NaN')
    print(set(df['Validated']))

    #standardize text case for Currency
    currency_mapping = {'USD': 'USD', 'usd': 'USD'}
    df['Currency'] = df['Currency'].map(currency_mapping, na_action='ignore').fillna('NaN')
    print(set(df['Currency']))

    #standardize text case for Exchange
    exchange_mapping = {'NASDAQ': 'NASDAQ', 'NYSE': 'NYSE'}
    df['Exchange'] = df['Exchange'].map(exchange_mapping, na_action='ignore').fillna('NaN')
    print(set(df['Exchange']))

    # #standardize text case for Ticker
    allowed_tickers = ['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA', 'TSLA']
    df['Ticker'] = df['Ticker'].where(df['Ticker'].isin(allowed_tickers))
    print(set(df['Ticker']))

    allowed_sectors = ['Automotive', 'Communication Services', 'Consumer Discretionary', 'Semiconductors', 'Technology']
    df['Sector'] = df['Sector'].where(df['Sector'].isin(allowed_sectors))
    print(set(df['Sector']))

    #standardized casing for Notes
    notes_mapping = {'EoD': 'EoD', 'gap down': 'Gap Down', 'gap up': 'Gap Up', 'pre-earnings': 'Pre-Earnings', 'rev miss': 'Rev Miss'}
    df['Notes'] = df['Notes'].map(notes_mapping, na_action='ignore').fillna('NaN')
    print(set(df['Notes']))

    #Numeric column cleaning
    numeric_columns = ['Open_Price', 'Close_Price', 'Volume']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # change date format
    df['Trade_Date'] = pd.to_datetime(df['Trade_Date'])

    # drop duplicates if any, then check schema
    # schema should have Trade_Date as dates, Open_Price, Close_Price, and Volume as floats
    # everything else is the same
    df = df.drop_duplicates()
    print(df)
    print(df.dtypes)

    # cleaned parquet
    df.to_parquet('cleaned.parquet')

if __name__ == "__main__":
    main()