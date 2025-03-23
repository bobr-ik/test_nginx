from fastapi import FastAPI
from time import time

app = FastAPI()

@app.get("/time")
def ping():
    return {"ans": time()}

