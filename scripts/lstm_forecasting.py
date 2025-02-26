import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("data/BrentOilPrices_Cleaned.csv", parse_dates=["Date"], index_col="Date")

# Sort data by date
df = df.sort_index()

# Normalize the price column
scaler = MinMaxScaler(feature_range=(0, 1))
df["Scaled_Price"] = scaler.fit_transform(df[["Price"]])

# Create sequences for time series forecasting
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

# Set sequence length
seq_length = 60  # Lookback period (e.g., 60 days)

# Split data into train/test sets
train_size = int(len(df) * 0.8)
train_data = df["Scaled_Price"][:train_size].values
test_data = df["Scaled_Price"][train_size - seq_length:].values  # Include last part of train for continuity

# Create sequences
X_train, y_train = create_sequences(train_data, seq_length)
X_test, y_test = create_sequences(test_data, seq_length)

# Reshape input for LSTM [samples, time steps, features]
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Build LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=1)

# Predictions
predictions = model.predict(X_test)

# Inverse transform to original scale
predictions = scaler.inverse_transform(predictions.reshape(-1, 1))
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test_actual, predictions))
print(f"Test RMSE: {rmse:.2f}")

# Plot actual vs predicted
plt.figure(figsize=(12,6))
plt.plot(df.index[train_size + seq_length:], y_test_actual, label="Actual Prices", color="blue")
plt.plot(df.index[train_size + seq_length:], predictions, label="LSTM Predictions", color="red")
plt.xlabel("Date")
plt.ylabel("Brent Oil Price (USD)")
plt.title("Brent Oil Price Prediction using LSTM")
plt.legend()
plt.show()
