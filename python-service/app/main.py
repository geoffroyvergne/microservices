from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/index")
def read_root():
    return {"message": "Python Service"}
