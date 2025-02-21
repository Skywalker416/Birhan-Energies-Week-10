import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the cleaned dataset
df = pd.read_csv("data/BrentOilPrices_Cleaned.csv", parse_dates=['Date'], index_col='Date')

# Fit ARIMA Model
model = ARIMA(df['Price'], order=(5,1,0))  # (p,d,q) parameters
model_fit = model.fit()

# Forecast the next 30 days
forecast = model_fit.forecast(steps=30)

# Plot results
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Price'], label="Historical Prices")
plt.plot(pd.date_range(df.index[-1], periods=30, freq='D'), forecast, label="Forecast", color='red')
plt.xlabel("Date")
plt.ylabel("Price (USD per barrel)")
plt.title("Brent Oil Price Forecast")
plt.legend()
plt.show()

print(model_fit.summary())
