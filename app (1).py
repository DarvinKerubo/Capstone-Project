
import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Function to load the ARIMA model
def load_arima_model():
    try:
        # Load the ARIMA model from file
        model = sm.load('arima_model.pkl')
        return model
    except FileNotFoundError:
        st.error("ARIMA model not found. Please make sure you have saved the model.")
        return None

# Function to load data_diff from CSV
def load_data_diff():
    try:
        data_diff = pd.read_csv('data_diff.csv')
        return data_diff
    except FileNotFoundError:
        st.error("data_diff.csv not found. Please make sure you have saved the file.")
        return None

# Function to make forecasts using the ARIMA model
def make_arima_forecasts(model, horizon):
    try:
        # Perform forecasts using the ARIMA model
        forecasts = model.forecast(steps=horizon)
        return forecasts
    except Exception as e:
        st.error(f"An error occurred while making forecasts: {str(e)}")
        return None

def main():
    st.title('ARIMA Time Series Forecasting')

    # Load the ARIMA model
    arima_model = load_arima_model()
    if arima_model is None:
        st.stop()

    # Load the data_diff
    data_diff = load_data_diff()
    if data_diff is None:
        st.stop()

    # Display the current data_diff
    st.subheader('Differenced Time Series Data')
    st.write(data_diff)  # Display the differenced time series data

    # Get user input for the forecasting horizon
    max_horizon = len(data_diff)  # Maximum allowed horizon is the length of the available data
    horizon = st.number_input('Enter the forecasting horizon:', value=10, min_value=1, max_value=max_horizon, step=1)

    # Make forecasts using the ARIMA model
    forecasts = make_arima_forecasts(arima_model, horizon)
    if forecasts is None:
        st.stop()

    # Create a DataFrame to display the forecasts
    last_date = data_diff.index[-1]
    forecast_dates = pd.date_range(start=last_date, periods=horizon + 1, closed='right')
    forecast_values = np.concatenate(([data_diff.iloc[-1]], forecasts))
    forecast_df = pd.DataFrame({'Forecast': forecast_values}, index=forecast_dates)

    # Display the forecasts as a graph
    st.subheader('ARIMA Forecasts')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_diff.index, data_diff['Original'], label='Original Data')
    ax.plot(forecast_dates, forecast_values, label='Forecasts', linestyle='--', color='orange')
    ax.set_xlabel('Date')
    ax.set_ylabel('Differenced Value')
    ax.legend()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
