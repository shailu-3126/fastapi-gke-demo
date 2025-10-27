from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on GKE!"}

@app.get("/health")
def health():
    return {"status": "ok"}
