# Dual API System (Python FastAPI)

A simple two-API system where API1 forwards requests to API2 and returns the response back to the client.

## Architecture

- **API1**: Runs on port 8001, receives client requests and forwards them to API2
- **API2**: Runs on port 8002, processes requests from API1 and returns responses

## Prerequisites

- Docker
- Docker Compose

## How to Deploy

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd dual-api-system
   ```

2. Build and start the services using Docker Compose:
   ```bash
   docker compose up --build
   ```

3. The services will be available at:
   - API1: http://localhost:8001
   - API2: http://localhost:8002

## How to Test the APIs

### Test the main functionality (API1 → API2 flow)

Send a request to API1, which will forward it to API2:

```bash
curl http://localhost:8001/api/message
```

Expected response:
```json
{
  "message": "Response from API1",
  "api2_response": {
    "message": "Hello from API2!",
    "processed_at": "2024-01-01T12:00:00.000000",
    "data": "This is the response from API2"
  },
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

### Test individual APIs

Test API1 health check:
```bash
curl http://localhost:8001/health
```

Test API2 directly:
```bash
curl http://localhost:8002/health
curl http://localhost:8002/api/process
```

### Interactive API Documentation

FastAPI provides automatic interactive documentation:
- API1 docs: http://localhost:8001/docs
- API2 docs: http://localhost:8002/docs

## Viewing Logs

To see the log messages from both APIs, run:
```bash
docker compose logs -f
```

You should see log messages like:
- `[API1] Received request for /api/message`
- `[API1] Forwarding request to API2...`
- `[API2] Received request from API1`
- `[API2] Processing request...`

## Stopping the Services

To stop the services:
```bash
docker compose down
```

## Project Structure

```
.
├── api1/
│   └── main.py            # API1 server code
├── api2/
│   └── main.py            # API2 server code
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile.api1        # Dockerfile for API1
├── Dockerfile.api2        # Dockerfile for API2
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **httpx**: Async HTTP client for making requests between APIs
- **Docker**: Containerization platform