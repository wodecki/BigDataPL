# Iowa Sales Time Series Prediction Models

This project uses AutoGluon to train and predict time series models for Iowa sales data.

## Files

- `1. train.py` - Trains the AutoGluon time series model and saves prediction plots
- `2. predict.py` - Loads trained model and makes predictions with detailed output
- `main.py` - Basic hello world script
- `pyproject.toml` - Project dependencies and configuration

## Requirements

- Python 3.8-3.12 (Python 3.13 not supported due to Ray dependency)
- Dependencies: pandas, autogluon.timeseries, matplotlib

## Usage

### Training the Model

```bash
uv run --python 3.12 "1. train.py"
```

This will:
- Load `data/iowa_sales.csv`
- Train an AutoGluon time series predictor
- Save the model to `autogluon-iowa-daily/`
- Generate and save prediction plots as `predictions_plot.png` and `predictions_plot.pdf`

### Making Predictions

```bash
uv run --python 3.12 "2. predict.py"
```

This will:
- Load the trained model
- Make predictions on current data
- Generate future predictions (3 months ahead)
- Print detailed prediction summaries for all items

## Data

The model expects `data/iowa_sales.csv` with columns:
- `date` - timestamp column
- `item_name` - item identifier
- `total_amount_sold` - target variable

## Output

- **Model**: Saved in `autogluon-iowa-daily/` directory
- **Plots**: `predictions_plot.png` and `predictions_plot.pdf`
- **Predictions**: Printed to console with detailed summaries