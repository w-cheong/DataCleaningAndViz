import pandas as pd

def main():
    df = pd.read_parquet("cleaned.parquet")
    
    # aggregate average open price of sector
    agg1 = (
        df.groupby('Sector')
        .agg({"Open_Price": "mean"})
        .rename(columns={"Open_Price": "Avg_Open_Price"})
        .sort_values("Avg_Open_Price", ascending=False)
    )

    # aggregate average volume of ticker
    agg2 = (
        df.groupby('Ticker')
        .agg({"Volume": "mean"})
        .rename(columns={"Volume": "Avg_Volume"})
        .sort_values("Avg_Volume", ascending=False)
    )
    
    # aggregate average close price of trade date
    agg3 = (
        df.groupby('Trade_Date')
        .agg({"Close_Price": "mean"})
        .rename(columns={"Close_Price": "Avg_Close_Price"})
        .sort_values("Avg_Close_Price", ascending=False)
    )
    
    agg1.to_parquet('agg1.parquet')
    agg2.to_parquet('agg2.parquet')
    agg3.to_parquet('agg3.parquet')

    agg1 = pd.read_parquet("agg1.parquet")
    agg2 = pd.read_parquet("agg2.parquet")
    agg3 = pd.read_parquet("agg3.parquet")

if __name__ == "__main__":
    main()