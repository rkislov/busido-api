from fastapi import FastAPI
from core.config import settings
from db.sessions import engine
from db.base_class import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

@app.get("/")
async def hello_api():
    return {"msg": "Hello, BusidoAPI"}
