from fastapi import FastAPI
from app.routers.devices import router as devices_router

app = FastAPI(
    title="NetPilot API",
    description="Network automation and monitoring platform",
    version="0.1.0",
)


app.include_router(devices_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "NetPilot API"
    }
    
    
