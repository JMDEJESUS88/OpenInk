from fastapi import FastAPI

app = FastAPI(
    title="OpenInk",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "OpenInk",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }