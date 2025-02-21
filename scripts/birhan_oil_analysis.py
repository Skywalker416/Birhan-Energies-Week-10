import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from statsmodels.tsa.stattools import adfuller
from ruptures import Pelt, Binseg, CostRbf

# Load the dataset
file_path = "/mnt/data/BrentOilPrices.csv"
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# Sort the dataset by date
df = df.sort_values(by='Date').reset_index(drop=True)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# Exploratory Data Analysis
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='Brent Oil Price', color='blue')
plt.xlabel('Year')
plt.ylabel('Price (USD per Barrel)')
plt.title('Brent Oil Price Over Time')
plt.legend()
plt.show()

# Check for stationarity using Augmented Dickey-Fuller test
def adf_test(series):
    result = adfuller(series.dropna())
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:", result[4])
    if result[1] <= 0.05:
        print("The data is stationary")
    else:
        print("The data is non-stationary")

adf_test(df['Price'])

# Change Point Detection
algo = Pelt(model="rbf").fit(df['Price'].values)
change_points = algo.predict(pen=10)
print("Detected change points:", change_points)

# Plot detected change points
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='Brent Oil Price', color='blue')
for cp in change_points:
    plt.axvline(df['Date'].iloc[cp], color='red', linestyle='--', label='Change Point' if cp == change_points[0] else "")
plt.xlabel('Year')
plt.ylabel('Price (USD per Barrel)')
plt.title('Brent Oil Price with Detected Change Points')
plt.legend()
plt.show()
