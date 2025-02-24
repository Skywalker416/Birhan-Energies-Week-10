import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def train_lstm(data_path, epochs=50):
    # Load dataset
    df = pd.read_csv(data_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df[['Brent_Oil_Price']])

    # Prepare training data
    X, y = [], []
    for i in range(len(df_scaled)-10):
        X.append(df_scaled[i:i+10])
        y.append(df_scaled[i+10])

    X, y = np.array(X), np.array(y)

    # Define LSTM model
    model = Sequential([
        LSTM(50, activation='relu', return_sequences=True, input_shape=(10,1)),
        LSTM(50, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=epochs, verbose=1)

    return model

if __name__ == "__main__":
    trained_model = train_lstm('data/BrentOilPrices_Cleaned.csv')
    print("LSTM model trained successfully.")
