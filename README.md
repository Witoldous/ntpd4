# ntpd4
## Setup and Installation

### Running Locally (Without Docker)
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ml-api-docker.git
   cd ml-api-docker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   API will be available at [http://localhost:8000](http://localhost:8000).

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t fastapi-ml .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 fastapi-ml
   ```

### Running with Docker Compose
1. Start the application and the database (Redis):
   ```sh
   docker-compose up --build
   ```

### Environment Variables
- `PORT` – Server port (default: 8000)
- `REDIS_HOST` – Redis host address
- `REDIS_PORT` – Redis port (default: 6379)

## Requirements
- Python 3.9+
- FastAPI, Uvicorn, Scikit-learn
- Docker & Docker Compose

## API Endpoints
- `GET /` - Welcome message
- `GET /info` - Model details
- `POST /predict` - Make a prediction (expects JSON with `features` array)

## Testing the API
Using `curl`:
```sh
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
