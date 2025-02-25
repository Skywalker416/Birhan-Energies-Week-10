import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_arima(df, steps=30):
    model = ARIMA(df['Brent_Oil_Price'], order=(5,1,0))
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=steps)
    return pd.DataFrame({"Date": pd.date_range(df.index[-1], periods=steps, freq='D'), "Forecast": forecast.values})
