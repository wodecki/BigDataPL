# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Google Cloud Run dynamically assigns the port, so make sure we listen on $PORT
ENV PORT=8003

# Command to run the application
CMD uvicorn main:app --host 0.0.0.0 --port $PORT