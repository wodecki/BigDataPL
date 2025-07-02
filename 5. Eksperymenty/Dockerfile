FROM python:3.10

# Copy the entire project directory
COPY . /app

WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Correctly format the CMD command to run Streamlit
CMD streamlit run app.py --server.port=$PORT --server.enableCORS=false --server.enableXsrfProtection=false --server.headless=true