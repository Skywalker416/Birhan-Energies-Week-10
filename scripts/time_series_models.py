import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(data_path, order=(5,1,0)):
    # Load dataset
    df = pd.read_csv(data_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Fit ARIMA model
    model = ARIMA(df['Brent_Oil_Price'], order=order)
    fitted_model = model.fit()

    # Forecast next 30 days
    forecast = fitted_model.forecast(steps=30)
    return forecast

if __name__ == "__main__":
    forecasted_values = arima_forecast('data/BrentOilPrices_Cleaned.csv')
    print("Forecasted Prices:\n", forecasted_values)
