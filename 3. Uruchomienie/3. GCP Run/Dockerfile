FROM python:3.10

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy pyproject.toml and uv.lock first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen

# Copy the entire project directory
COPY . /app

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define environment variable
ENV MODULE_NAME="main"
ENV VARIABLE_NAME="app"
ENV PORT=8003

# Run app.py when the container launches using uv run
CMD ["sh", "-c", "uv run uvicorn main:app --host 0.0.0.0 --port $PORT"]