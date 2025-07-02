import streamlit as st
import requests
import pandas as pd

# Define the URL of your FastAPI endpoint
API_URL = "http://localhost:8003/predict/"

def get_predictions(item_name):
    """Send a GET request to the FastAPI server to get predictions."""
    response = requests.get(f"{API_URL}{item_name}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title('Alcohol Sales Prediction')
    item_name = st.selectbox(
        'Select an Item',
        ('BLACK VELVET', 'FIREBALL CINNAMON WHISKEY', 'HAWKEYE VODKA', 'TITOS HANDMADE VODKA', 'FIVE O\'CLOCK VODKA')
    )
    
    if st.button('Predict Sales'):
        predictions = get_predictions(item_name)
        if predictions:
            # Convert predictions to DataFrame
            prediction_data = predictions.get('predictions')
            if prediction_data:
                df = pd.DataFrame(prediction_data)
                # Format the timestamp to only display year-month-day
                df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
                df.rename(columns={'timestamp': 'Date', 'mean': 'Mean Sales'}, inplace=True)
                st.write('Predictions for the next 7 days:')
                st.table(df)
            else:
                st.write("No prediction data available.")
        else:
            st.error('Failed to retrieve predictions. Make sure the FastAPI server is running.')

if __name__ == '__main__':
    main()
