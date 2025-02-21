import pandas as pd

# Load the dataset
file_path = "data/BrentOilPrices.csv"
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# Sort data by date
df = df.sort_values(by='Date')

# Check for missing values
df = df.dropna()

# Save cleaned data
df.to_csv("data/BrentOilPrices_Cleaned.csv", index=False)

print("Data preprocessing complete. Cleaned dataset saved.")
