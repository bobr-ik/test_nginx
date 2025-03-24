from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import time
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://77.222.54.5"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/time")
def ping():
    return {"ans": time()}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)