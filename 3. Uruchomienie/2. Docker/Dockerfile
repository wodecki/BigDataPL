FROM python:3.10

# Copy the entire project directory
COPY . /app

WORKDIR /app

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define environment variable
ENV MODULE_NAME="main"
ENV VARIABLE_NAME="app"
ENV PORT=8003

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]