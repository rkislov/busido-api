from fastapi import FastAPI, Request, Response
from core.config import settings
from apis.base import api_router
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_pagination import add_pagination

from redis import asyncio as aioredis

def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
#    create_tables()
    include_router(app)
    add_pagination(app)
    return app


app = start_application()



@app.get("/")
async def hello_api():
    return {"msg": "Hello, BusidoAPI"}


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")