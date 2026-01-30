from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="fastapi_demo", version= "0.1.0")

class StatusResponse(BaseModel):
    status: str
    build: Optional [str] = None

@app.get("/", response_model=StatusResponse)

def read_root():
    return {"status":"OK", "Build": "dev"}