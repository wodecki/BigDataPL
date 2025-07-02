lokalnie:
docker build . -t chat
docker run -d -p 8000:8000 chat

GCP run:
1. Dla pierwszej wersji app.py:
docker build . --platform linux/amd64 -t chat
docker tag chat europe-west4-docker.pkg.dev/asi2024-415408/bigdata/chat:latest
docker push europe-west4-docker.pkg.dev/asi2024-415408/bigdata/chat:latest

2. Deploy to GCP Run

3. Zmień wersję app.py
docker build . --platform linux/amd64 -t chat
docker tag chat europe-west4-docker.pkg.dev/asi2024-415408/bigdata/chat:latest
docker push europe-west4-docker.pkg.dev/asi2024-415408/bigdata/chat:latest

4. Edit and Deploy a New Revision

5. Manage traffic > 80/20
