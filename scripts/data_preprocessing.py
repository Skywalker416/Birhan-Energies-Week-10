import pandas as pd

def load_and_clean_data(oil_price_path, economic_data_path=None):
    # Load oil prices dataset
    df = pd.read_csv(oil_price_path, parse_dates=['Date'], dayfirst=True)
    df = df.rename(columns={'Price': 'Brent_Oil_Price'})
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Handle missing values
    df = df.dropna()

    if economic_data_path:
        # Load economic indicators (if available)
        econ_df = pd.read_csv(economic_data_path, parse_dates=['Date'], dayfirst=True)
        
        # Merge datasets on Date
        df = pd.merge(df, econ_df, on='Date', how='left')

    return df

if __name__ == "__main__":
    data = load_and_clean_data('data/BrentOilPrices.csv', 'data/economic_factors.csv')
    data.to_csv('data/BrentOilPrices_Cleaned.csv', index=False)
    print("Data preprocessing complete. Cleaned file saved.")
