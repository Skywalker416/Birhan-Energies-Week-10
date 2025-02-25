# Change Point Analysis and Statistical Modeling of Brent Oil Prices

## Project Overview
This project analyzes **Brent oil price fluctuations** over time by detecting key change points and applying statistical modeling. The goal is to understand how major events (e.g., geopolitical crises, OPEC policy changes) impact oil prices and provide insights for investors, policymakers, and energy companies.

## Objectives
- **Perform Exploratory Data Analysis (EDA)**
- **Detect significant price change points using PELT algorithm**
- **Apply ARIMA model for time series forecasting**
- **Provide data-driven insights for decision-makers**


---

## ✅ Task 1: Data Analysis & Understanding
### 📊 Workflow & Data Understanding
- **Dataset**: Historical Brent oil prices (May 1987 - Sept 2022).
- **Preprocessing**: Cleaned missing values and normalized date format.
- **Exploratory Data Analysis (EDA)**:
  - Trends and seasonality examined.
  - Price distributions visualized.
- **Time Series Modeling**:
  - ARIMA (forecasting).
  - GARCH (volatility analysis).
  - LSTM (deep learning).

### 🔍 Understanding Models
- **ARIMA**: Captures trend and seasonality in time series.
- **GARCH**: Detects price volatility and risk.
- **LSTM**: Uses neural networks to model long-term dependencies.

---

## 📊 Task 2: Advanced Statistical Analysis & Machine Learning
### 📈 Additional Models & Techniques
- **VAR (Vector Autoregression)**: Multivariate time series analysis.
- **Markov-Switching ARIMA**: Identifies market condition shifts.
- **LSTM**: Captures non-linear dependencies in oil price movement.

### 🌎 External Influences on Oil Prices
- **Economic Indicators**: GDP, inflation, unemployment, exchange rates.
- **Technological Innovations**: Fracking, renewable energy impact.
- **Political & Regulatory Factors**: OPEC policies, trade sanctions.

### 🏆 Model Validation
- **Backtesting**: Assesses model accuracy on past data.
- **Performance Metrics**: RMSE, MAE, R².

---

## 📊 Task 3: Interactive Dashboard Development
### 🛠 Backend (Flask)
- **API Endpoints**:
  - `/api/prices`: Serves historical price data.
  - `/api/events`: Provides significant global events.
  - `/api/forecast`: Returns future price predictions.

### 💻 Frontend (React)
- **Visualizations**:
  - Interactive line charts for oil prices.
  - Event markers highlighting historical impacts.
- **User Controls**:
  - Date range filters.
  - Event comparison tools.

---

## 🚀 Installation & Execution
### ✅ Prerequisites
- **Backend**: Python 3.8+, Flask, Pandas, Scikit-learn.
- **Frontend**: Node.js 14+, React, Recharts.

### 🔧 Running the Project
#### Backend
```sh
cd backend
pip install -r requirements.txt
python app.py
---
```
## 📂 **Project Structure**  

```plaintext
BrentOilPriceAnalysis/
├── backend/
│   ├── app.py
│   ├── data_processing.py
│   ├── models.py
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── ...
│   ├── package.json
│   └── node_modules/
├── notebooks/
│   ├── eda.ipynb
│   ├── changepoint_detection.ipynb
│   ├── model_training.ipynb
├── data/
│   ├── raw/
│   │   └── BrentOilPrices.csv
│   ├── processed/
│   │   └── BrentOilPrices_Cleaned.csv
├── scripts/
│   ├── data_preprocessing.py
│   ├── change_point_detection.py
│   └── model_training.py
└── README.md
```

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/Brent_Oil_Analysis.git
   cd Brent_Oil_Analysis
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run scripts as needed:
   - **Data Preprocessing:** `python scripts/data_preprocessing.py`
   - **Change Point Detection:** `python scripts/change_point_detection.py`
   - **Model Training:** `python scripts/model_training.py`

## Implementation Details

### 1. Data Preprocessing (`data_preprocessing.py`)
- Converts the `Date` column to datetime format.
- Sorts and cleans the data.
- Saves the cleaned dataset as `BrentOilPrices_Cleaned.csv`.

### 2. Exploratory Data Analysis (`EDA.ipynb`)
- Visualizes Brent oil price trends over time.
- Performs **Augmented Dickey-Fuller (ADF) test** to check stationarity.

### 3. Change Point Detection (`change_point_detection.py`)
- Uses **PELT algorithm** (`ruptures` library) to detect structural breaks in price trends.
- Plots detected change points.

### 4. Time Series Forecasting (`model_training.py`)
- Implements **ARIMA model** to predict future oil prices.
- Plots historical vs. forecasted prices.

## Results & Insights
1. **Change Point Analysis** identified major price shifts linked to **geopolitical events and economic policies**.
2. **ARIMA Forecasting** provided potential future price trends.
3. The project delivers **data-driven insights** for energy market stakeholders.

## Future Work
- Implement **GARCH models** for volatility analysis.
- Extend the dataset with **economic indicators (inflation, interest rates, etc.)**.
- Build a **real-time dashboard** for better visualization.

## Contributors
- Amanuel Legesse - Lead Developer

## License
This project is licensed under the MIT License.

---
