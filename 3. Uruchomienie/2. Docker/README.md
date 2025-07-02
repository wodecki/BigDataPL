# Iowa Sales Prediction Docker Setup

This Docker setup uses **uv** as the package manager with `pyproject.toml` for dependency management.

## Prerequisites
- Docker installed on your system
- uv package manager (for local development)

## Build and Run

1. **Build the image:**
   ```bash
   docker build . -t iowa-uv
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8003:8003 --name iowa_container iowa-uv
   ```

3. **Test the API:**
   ```bash
   curl "http://localhost:8003/predict/BLACK%20VELVET"
   ```

4. **Stop the container:**
   ```bash
   # Find the container ID
   docker ps
   
   # Stop and remove the container
   docker kill iowa_container
   docker rm iowa_container
   ```

## Available Items for Prediction
- BLACK VELVET
- FIREBALL CINNAMON WHISKEY  
- HAWKEYE VODKA
- TITOS HANDMADE VODKA
- FIVE O'CLOCK VODKA

## Docker Configuration
- Uses **uv** package manager for faster dependency resolution
- Dependencies defined in `pyproject.toml`
- Lockfile (`uv.lock`) ensures reproducible builds
- FastAPI application runs on port 8003
