Build the image: 
docker build . --platform linux/amd64 -t iowa

Tag the image:
docker tag iowa:latest europe-west4-docker.pkg.dev/asi2024-415408/bigdata/iowa:latest < change to Your registry

Push the image to the registry:
docker push europe-west4-docker.pkg.dev/asi2024-415408/bigdata/iowa:latest < change to Your registry

Deploy on Google Cloud Run

Query:
curl "https://iowa2-944177704287.europe-west4.run.app/predict/BLACK%20VELVET" < change the servise address!

Run streamlit app:
modify app.py:
change API_URL = "http://localhost:8003/predict/" to API_URL = "https://iowa-944177704287.europe-west4.run.app/predict/"

uv run streamlit run app.py