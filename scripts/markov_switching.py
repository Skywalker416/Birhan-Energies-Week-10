import pandas as pd
import numpy as np
import statsmodels.api as sm

def markov_switching_analysis(data_path):
    # Load dataset
    df = pd.read_csv(data_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Fit Markov-Switching model
    mod = sm.tsa.MarkovRegression(df['Brent_Oil_Price'], k_regimes=2, trend='c', switching_variance=True)
    res = mod.fit()

    return res.summary()

if __name__ == "__main__":
    summary = markov_switching_analysis('data/BrentOilPrices_Cleaned.csv')
    print(summary)
