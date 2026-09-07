from fastapi import FastAPI

app = FastAPI(
    title="NetPilot API",
    description="Network automation and monitoring platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "NetPilot API"
    }