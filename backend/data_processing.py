import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    return df

def get_event_impact(df):
    # Simulated function to return historical event impact
    events = [
        {"date": "2020-03-01", "event": "COVID-19 Pandemic", "impact": "Price Drop"},
        {"date": "2022-02-24", "event": "Russia-Ukraine War", "impact": "Price Surge"},
    ]
    return events
