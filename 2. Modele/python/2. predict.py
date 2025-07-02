import pandas as pd
from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor

df = pd.read_csv("data/iowa_sales.csv")

#transform the date column to timestamp
df['date'] = pd.to_datetime(df['date'])

train_data = TimeSeriesDataFrame.from_data_frame(
    df,
    id_column="item_name",
    timestamp_column="date"
)

predictor = TimeSeriesPredictor.load("autogluon-iowa-daily")
predictions = predictor.predict(train_data)

print("=== Current Predictions ===")
print(predictions.head())
print(f"Predictions shape: {predictions.shape}")

#get "mean" for the max value of timestamp in df for item_id = "BLACK VELVET"

# Filter the predictions for 'BLACK VELVET'
black_velvet_predictions = predictions.loc['BLACK VELVET']

# Find the maximum timestamp for 'BLACK VELVET'
max_timestamp = black_velvet_predictions.index.max()
# Get the 'mean' value for the maximum timestamp
mean_value = black_velvet_predictions.loc[max_timestamp, 'mean']
print("Mean prediction for BLACK VELVET on the maximum timestamp (", max_timestamp, "):", mean_value)

#create a df_future by shifting date in df by 3 months
df_future = df.copy()
df_future['date'] = df_future['date'] + pd.DateOffset(months=3)

future_data = TimeSeriesDataFrame.from_data_frame(
    df_future,
    id_column="item_name",
    timestamp_column="date"
)

future_predictions = predictor.predict(future_data)
print("\n=== Future Predictions (3 months ahead) ===")
print(future_predictions.head())
print(f"Future predictions shape: {future_predictions.shape}")

print("\n=== All Items Future Predictions Summary ===")
for item in future_predictions.index.get_level_values(0).unique():
    item_pred = future_predictions.loc[item]
    max_ts = item_pred.index.max()
    mean_val = item_pred.loc[max_ts, 'mean']
    print(f"{item}: {mean_val:.2f} (on {max_ts})")
