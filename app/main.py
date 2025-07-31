from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from my app!"}

@app.get("/health")
def health():
    return {"status": "ok", "database": os.getenv("DATABASE_URL", "not set")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
