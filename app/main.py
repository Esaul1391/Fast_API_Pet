import asyncio

from fastapi import FastAPI, Query, Depends
from fastapi.staticfiles import StaticFiles  # работа с файлами
from fastapi.middleware.cors import CORSMiddleware

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from app.images.router import router as router_images


async def get_cashe():
    while True:
        print('start')
        await asyncio.sleep(3)
        print('end')
@asynccontextmanager  # pip install "fastapi-cache2[redis]"
async def lifespan(app: FastAPI):
    # при запуске
    print('connect redis')
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    asyncio.create_task(get_cashe())
    print('Вот сейчас приложение запустится')
    yield
    # при выключении


app = FastAPI(
    lifespan=lifespan
)  # вызываю класс fastapi

app.mount('/static', StaticFiles(directory='app/static'), 'static')  # монтирование стат. контента
app.include_router(router_users)

app.include_router(router_bookings)
app.include_router(router_pages)

app.include_router(router_images)
# добавляю площадки которы могут обращаться к API

origins = [
    "http://localhoost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # разрушаю ориджин
    allow_credentials=True,  # отвечает за cookies
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: bool = Query(default=None),
            stars: int = Query(ge=1, le=5, default=None)  # >= 1 и <= 5
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get('/hotels')
def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    return search_args


class SHotel(BaseModel):
    address: str
    name: str
    stars: int

# class SBooking(BaseModel):  # поля для POST запроса СХЕМА
#     room_id: int
#     date_from: date
#     date_to: date
#
#
# @app.post("/bookings")
# def add_booking(booking: SBooking):
#     pass
