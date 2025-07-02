from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor

app = FastAPI()

# Load the model when starting the app
predictor = TimeSeriesPredictor.load("model", require_version_match=False) 

# Define a request body model
class ItemRequest(BaseModel):
    item_name: str

@app.get("/predict/{item_name}")
async def predict(item_name: str):
    df = pd.read_csv("data/iowa_sales.csv")
    df['date'] = pd.to_datetime(df['date'])
    train_data = TimeSeriesDataFrame.from_data_frame(
        df,
        id_column="item_name",
        timestamp_column="date"
    )
    predictions = predictor.predict(train_data)

    if item_name not in predictions.index.levels[0]:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_predictions = predictions.loc[item_name]
    max_timestamp = item_predictions.index.max()
    mean_value = item_predictions.loc[max_timestamp, 'mean']
    # Format the predictions into a list of dicts
    formatted_predictions = [
        {'timestamp': str(index), 'mean': row['mean']}
        for index, row in item_predictions.iterrows()
    ]
    return {'predictions': formatted_predictions}