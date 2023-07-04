from fastapi import FastAPI
from backend.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
async def hello_api():
    return {"msg": "Hello, BusidoAPI"}
