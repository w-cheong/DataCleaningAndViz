import pandas as pd

def main():
    df = pd.read_parquet("cleaned.parquet")
    print(df)
    
    #aggregations
    agg1 = (
        df.groupby('Sector')
        .agg({"Open_Price": "mean"})
        .rename(columns={"Open_Price": "Avg_Open_Price"})
        .sort_values("Avg_Open_Price", ascending=False)
    )
    print(agg1)

    agg2 = (
        df.groupby('Ticker')
        .agg({"Volume" : "mean"})
        .sort_values("Volume", ascending=False)
    )
    print(agg2)
    
    agg3 = (
        df.groupby('Trade_Date')
        .agg({"Close_Price": "mean"})
        .rename(columns={"Close_Price": "Avg_Close_Price"})
        .sort_values("Avg_Close_Price", ascending=False)
    )
    print(agg3)
    
    df.to_parquet('agg1.parquet')
    df.to_parquet('agg2.parquet')
    df.to_parquet('agg3.parquet')

if __name__ == "__main__":
    main()