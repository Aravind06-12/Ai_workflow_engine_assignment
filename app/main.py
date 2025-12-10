# app/main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Mini Workflow Engine is up. Use /docs for Swagger UI."}
