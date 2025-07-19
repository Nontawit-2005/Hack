import os
from datetime import datetime
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="API2")

PORT = int(os.getenv("PORT", 8002))

@app.get("/health")
async def health_check():
    print("[API2] Health check requested")
    return {
        "status": "API2 is running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/hello")
async def hello_from_api2():
    print(f"[API2] Received request at /hello - {datetime.now().isoformat()}")
    return {
        "from": "API2",
        "message": "Hello World",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/process")
async def process_request():
    print("[API2] Received request from API1")
    print("[API2] Processing request...")
    
    response = {
        "message": "Hello from API2!",
        "processed_at": datetime.now().isoformat(),
        "data": "This is the response from API2"
    }
    
    print("[API2] Sending response back to API1")
    return response

if __name__ == "__main__":
    print(f"[API2] Server starting on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)