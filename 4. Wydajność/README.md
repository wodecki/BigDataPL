0. zainstaluj locust: `pip install locust`
1. uruchom swój serwis lokalnie
conda activate automl
uvicorn main:app --reload --host 0.0.0.0 --port 8003
`curl "http://localhost:8003/predict/BLACK%20VELVET"

2. w miejscu, gdzie jest `locustfile.py`
   - ​      `locust`    
3. w interfejsie www
   - no of users: 1000
   - ramp-up: 50
   - jako host wpisz
     - dla testu VM: `http://localhost:8003` < zmień adres
     - dla usługi GCP Run: `https://iowa-fne6tu3xva-ez.a.run.app` < zmień adres