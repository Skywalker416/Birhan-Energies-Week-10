# Change Point Analysis and Statistical Modeling of Brent Oil Prices

## Project Overview
This project analyzes **Brent oil price fluctuations** over time by detecting key change points and applying statistical modeling. The goal is to understand how major events (e.g., geopolitical crises, OPEC policy changes) impact oil prices and provide insights for investors, policymakers, and energy companies.

## Objectives
- **Perform Exploratory Data Analysis (EDA)**
- **Detect significant price change points using PELT algorithm**
- **Apply ARIMA model for time series forecasting**
- **Provide data-driven insights for decision-makers**

## Directory Structure
```
Brent_Oil_Analysis/
│-- data/
│   ├── BrentOilPrices.csv  # Raw dataset
│   ├── BrentOilPrices_Cleaned.csv  # Processed dataset
│-- notebooks/
│   ├── EDA.ipynb  # Exploratory Data Analysis
│   ├── ChangePointAnalysis.ipynb  # Change point detection
│   ├── TimeSeriesModeling.ipynb  # Forecasting Brent oil prices
│-- scripts/
│   ├── data_preprocessing.py  # Data loading & preprocessing
│   ├── change_point_detection.py  # Detecting key events affecting prices
│   ├── model_training.py  # ARIMA time series forecasting
│-- reports/
│   ├── analysis_report.pdf  # Summary of findings
│-- README.md  # Project documentation
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
- **Your Name** - Lead Developer

## License
This project is licensed under the MIT License.

---
