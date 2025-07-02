0. Activate environment: `conda activate asi`.
1. server startup: `uvicorn main:app --reload --host 0.0.0.0 --port 8003`.
2.1. query: in browser: `http://localhost:8003/predict/BLACK%20VELVET`
2.2. curl query: `curl "http://localhost:8003/predict/BLACK%20VELVET"`
3. streamlit application: `streamlit run app.py`.