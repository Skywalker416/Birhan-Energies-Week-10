from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from data_processing import load_data, get_event_impact
from models import forecast_arima

app = Flask(__name__)
CORS(app)

# Load data
data = load_data('data/BrentOilPrices_Cleaned.csv')

@app.route('/api/prices', methods=['GET'])
def get_prices():
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    event_impact = get_event_impact(data)
    return jsonify(event_impact)

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    forecast = forecast_arima(data)
    return jsonify(forecast.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
