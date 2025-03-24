from fastapi import FastAPI
from time import time
import uvicorn

app = FastAPI()

@app.get("/time")
def ping():
    return {"ans": time()}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)