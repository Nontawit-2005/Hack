import os
import httpx
from datetime import datetime
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="API1")

PORT = int(os.getenv("PORT", 8001))
API2_URL = os.getenv("API2_URL", "http://api2:8002")

@app.get("/health")
async def health_check():
    print("[API1] Health check requested")
    return {
        "status": "API1 is running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/message")
async def get_message():
    try:
        print("[API1] Received request for /api/message")
        print("[API1] Forwarding request to API2...")
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API2_URL}/api/process")
            response.raise_for_status()
            api2_data = response.json()
        
        print(f"[API1] Received response from API2: {api2_data}")
        print("[API1] Sending response back to client")
        
        return {
            "message": "Response from API1",
            "api2_response": api2_data,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as error:
        print(f"[API1] Error forwarding request to API2: {str(error)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Failed to communicate with API2",
                "details": str(error)
            }
        )

if __name__ == "__main__":
    print(f"[API1] Server starting on port {PORT}")
    print(f"[API1] Will forward requests to: {API2_URL}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)